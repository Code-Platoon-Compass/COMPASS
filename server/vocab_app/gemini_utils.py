"""
Utility functions for generating and retrieving vocabulary lists using the Gemini API.

This module handles:
- Pydantic schemas for structured Gemini responses
- Redis caching to avoid redundant DB lookups and API calls
- Gemini API integration for generating vocab lists from lecture URLs
- Persisting generated vocab lists and items to the database
"""
from google import genai
from pydantic import BaseModel
from .models import VocabItem, VocabList
from django.core.cache import cache
import os

class VocabListItemSchema(BaseModel):
    """Represents a single vocab item returned by Gemini."""
    term: str
    definition: str
class VocabListSchema(BaseModel):
    """Represents the full vocab list returned by Gemini."""
    items: list[VocabListItemSchema]
   
CACHE_TTL = 60 * 60 * 24  # 24 hours in seconds

# Temporary disable until GEMINI_API_KEY is available.
# client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))
client = None

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
        Given a url to a lecture, return a list of no more than 13 vocab terms and their definitions that 
        are relevant to the lecture material. 
"""

def get_vocab_list(lecture_url: str) -> VocabList | None:
    """
    Retrieve an existing vocab list for a given lecture URL.

    Checks Redis cache first. On a cache miss, queries the database.
    If found in the database, caches the result for 24 hours.

    Args:
        lecture_url: The URL of the lecture to look up.

    Returns:
        The VocabList instance if it exists, otherwise None.
    """
    cached = cache.get(lecture_url)
    if cached:
        return cached 
    
    vocab_list = VocabList.objects.filter(lecture_url=lecture_url).first()
    
    if vocab_list:
        cache.set(lecture_url, vocab_list, timeout=CACHE_TTL)  # Cache for 24 hours
        return vocab_list
    return None

def generate_vocab_list(lecture_url: str) -> VocabList:
    """
    Generate a vocab list for a given lecture URL using the Gemini API.

    Sends the lecture URL to Gemini with a structured prompt. Parses the
    response and saves the resulting VocabList and VocabItems to the database.
    Caches the VocabList in Redis for 24 hours.

    Args:
        lecture_url: The URL of the lecture to generate vocab for.

    Returns:
        The newly created VocabList instance.
    """
    prompt = f"{PROMPT}\nLECTURE_URL: {lecture_url}"
    if client is None:
        raise RuntimeError('Gemini integration is temporarily disabled until GEMINI_API_KEY is available.')

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