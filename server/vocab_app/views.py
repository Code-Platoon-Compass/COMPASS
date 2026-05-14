from django.core.cache import cache
from .models import VocabList
from .gemini_utils import get_vocab_list, generate_vocab_list
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import VocabItemSerializer
from rest_framework import status as s
import re


class VocabListView(APIView):
    """
    API view for managing vocabulary lists.

    Endpoints:
        POST   api/v1//vocab/  - Retrieve or generate a vocab list for a given lecture URL
        DELETE api/v1/vocab/  - Delete one or more vocab lists by their lecture URLs
    """

    def post(self, request):
        """
        Retrieve or generate a vocabulary list for a given lecture URL.

        If a vocab list already exists in cache or the database for the URL, it is returned.
        Otherwise, a new vocab list is generated via Gemini and returned.
        
        # Regex validates lecture_url starts with "http://3.12.198.12/"

        Request body:
            {
                "lecture_url": "https://codeplatoon.github.io/"
            }

        Returns:
            200 - List of vocab items (term + definition) for the lecture
            400 - Missing or invalid lecture_url
        """
        lecture_url = self.request.data.get('lecture_url')
        
        if not lecture_url:
            return Response({"error": "lecture_url is required"}, status= s.HTTP_400_BAD_REQUEST)
        
        r = '^https://codeplatoon.github.io/'
        
        if not re.match(r, lecture_url):
            return Response({"error": "Invalid lecture_url"}, status= s.HTTP_400_BAD_REQUEST)
        
        vocab_list = get_vocab_list(lecture_url)
        
        if vocab_list:            
            ser_vocab_items = VocabItemSerializer(vocab_list.items.all(), many=True)
            
            return Response(ser_vocab_items.data , status = s.HTTP_200_OK)
        
        vocab_list = generate_vocab_list(lecture_url)
        
        ser_vocab_items = VocabItemSerializer(vocab_list.items.all(), many=True)
        
        return Response(ser_vocab_items.data, status = s.HTTP_200_OK)
    
    def delete(self, request):
        """
        Delete one or more vocabulary lists by their lecture URLs.

        Validates that each URL matches the expected host and exists in the database
        before deleting. If any URL is invalid or not found, the request is rejected
        before any deletions occur.

        Request body:
            {
                "lecture_urls": [
                    "https://codeplatoon.github.io/",
                    "https://codeplatoon.github.io/"
                ]
            }

        Returns:
            200 - All specified vocab lists deleted successfully
            400 - Missing, non-list, or invalid lecture_urls
            404 - One or more lecture_urls not found in the database
        """
        lecture_urls = self.request.data.get('lecture_urls')
        
        if not lecture_urls or not isinstance(lecture_urls, list):
            return Response({"error": "at least one lecture_url is required and lecture_urls must be a list"}, status= s.HTTP_400_BAD_REQUEST)
        
        r = '^https://codeplatoon.github.io/'
        
        for lecture_url in lecture_urls:
            if not re.match(r, lecture_url):
                return Response({"error": f"{lecture_url} is an invalid lecture_url"}, status= s.HTTP_400_BAD_REQUEST)
        
            elif not VocabList.objects.filter(lecture_url=lecture_url).first():
                return Response({"error": f"{lecture_url} does not exist"}, status= s.HTTP_404_NOT_FOUND)
            
        for lecture_url in lecture_urls:   
            if VocabList.objects.filter(lecture_url=lecture_url).first():
                vocab_list = VocabList.objects.filter(lecture_url=lecture_url).first()
                if cache.get(lecture_url):
                    cache.delete(lecture_url)  
                vocab_list.delete()  
                
        return Response({"message": "Vocab list deleted successfully"}, status=s.HTTP_200_OK)
        
       
