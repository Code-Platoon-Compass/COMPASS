from google import genai
from pydantic import BaseModel
from .models import VocabItem, VocabList
from django.core.cache import cache 
import os
class VocabListItemSchema(BaseModel):
    term: str
    definition: str    
class VocabListSchema(BaseModel):
   items: list[VocabItem]

GEMINI_MODEL = 'gemini-2.5-flash-lite'

CONFIG={
        "response_mime_type": "application/json",
        "response_schema": VocabList
    },

PROMPT = """
    ROLE: 
        You are a coding bootcamp instructor that looks over software engineering related lecture material 
        and generates a list of vocab words and their definitions for new students to review before the lecture.
    INSTRUCTION:
        Given a url to a lecture, return a list of vocab words and their definitions that are relevant to the lecture material. 
"""

client = genai.Client(api_key= os.getenv('GEMINI_API_KEY'))

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Explain how AI works in a few words",
)

# function needed to check if url with vocab list already exit in redis first then checks db 
def get_vocab_list(lecture_url: str) -> VocabList:
    pass

def generate_vocab_list(lecture_url: str) -> VocabList:
    prompt = f"{PROMPT}\nLECTURE_URL: {lecture_url}"
    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=PROMPT,
        config=CONFIG
    )
    parsed = response.parsed
    # need to also add to redis cache here with expiration time of 24 hours
    for item in parsed.items:
        VocabItem.objects.get_or_create(
            vocab_list_url=lecture_url,
            term=item.term,
            definition=item.definition
        )
    vocab_list = VocabList.objects.get_or_create(lecture_url=lecture_url)[0]
    
    return vocab_list