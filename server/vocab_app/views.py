from .models import  VocabItem, VocabList
from .gemini_utils import get_vocab_list, generate_vocab_list
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import VocabItemSerializer, VocabListSerializer
from rest_framework import status as s
import re


class VocabListView(APIView):
    def post (self,request):
        lecture_url = self.request.data.get('lecture_url')
        
        if not lecture_url:
            return Response({"error": "lecture_url is required"}, status= s.HTTP_400_BAD_REQUEST)
        
        r = '^http://3\.12\.198\.12.'
        
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
        lecture_urls = self.request.data.get('lecture_urls')
        
        if not lecture_urls or not isinstance(lecture_urls, list):
            return Response({"error": "at least one lecture_url is required and lecture_urls must be a list"}, status= s.HTTP_400_BAD_REQUEST)
        
        r = '^http://3\.12\.198\.12.'
        
        for lecture_url in lecture_urls:
            if not re.match(r, lecture_url):
                return Response({"error": f"{lecture_url} is an invalid lecture_url"}, status= s.HTTP_400_BAD_REQUEST)
        
            elif not VocabList.objects.filter(lecture_url=lecture_url).first():
                return Response({"error": f"{lecture_url} does not exist"}, status= s.HTTP_404_NOT_FOUND)
            
        for lecture_url in lecture_urls:   
            if VocabList.objects.filter(lecture_url=lecture_url).first():
                vocab_list = VocabList.objects.filter(lecture_url=lecture_url).first()
                vocab_list.delete()       
                
        return Response({"message": "Vocab list deleted successfully"}, status=s.HTTP_200_OK)
        
       