from google import genai
from pydantic import BaseModel
from .models import VocabItem, VocabList
from django.core.cache import cache 
import os
class VocabListItemSchema(BaseModel):
    term: str
    definition: str    
class VocabListSchema(BaseModel):
   items: list[VocabListItemSchema]
   
CACHE_TTL = 60 * 60 * 24  # 24 hours in seconds

client = genai.Client(api_key=os.getenv('GEMINI_API_KEY')) 

GEMINI_MODEL = 'gemini-2.5-flash-lite'

CONFIG={
        "response_mime_type": "application/json",
        "response_schema": VocabListSchema
    }

PROMPT = """
    ROLE: 
        You are a coding bootcamp instructor that looks over software engineering related lecture material 
        and generates a list of vocab words and their definitions for new students to review before the lecture.
    INSTRUCTION:
        Given a url to a lecture, return a list of vocab words and their definitions that are relevant to the lecture material. 
"""

# function checks if url with vocab list already exist in redis first then checks existence in db and caches it for 24 hours or returns None. 
def get_vocab_list(lecture_url: str) -> VocabList | None:
    cached = cache.get(lecture_url)
    if cached:
        return cached 
    
    vocab_list = VocabList.objects.filter(lecture_url=lecture_url).first()
    
    if vocab_list:
        cache.set(lecture_url, vocab_list, timeout=CACHE_TTL)  # Cache for 24 hours
        return vocab_list
    return None

def generate_vocab_list(lecture_url: str) -> VocabList:
    prompt = f"{PROMPT}\nLECTURE_URL: {lecture_url}"
    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
        config=CONFIG
    )
    parsed = response.parsed
    vocab_list = VocabList.objects.get_or_create(lecture_url=lecture_url)[0]
    for item in parsed.items:
        VocabItem.objects.get_or_create(
            vocab_list_url=vocab_list,
            term=item.term,
            definition=item.definition
        )
    cache.set(lecture_url, vocab_list, timeout=CACHE_TTL)  # Cache for 24 hours
    
    return vocab_list