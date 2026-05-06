from .models import  VocabItem, VocabList
from .gemini_utils import get_vocab_list, generate_vocab_list
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import VocabItemSerializer, VocabListSerializer
from rest_framework import status as s


class VocabListView(APIView):
    def post (self,request):
        lecture_url = self.request.data.get('lecture_url')
        
        if not lecture_url:
            return Response({"error": "lecture_url is required"}, status= s.HTTP_400_BAD_REQUEST)
        
        vocab_list = get_vocab_list(lecture_url)
        
        if vocab_list:            
            ser_vocab_items = VocabItemSerializer(vocab_list.items.all(), many=True)
            
            return Response(ser_vocab_items.data , status = s.HTTP_200_OK)
        
        vocab_list = generate_vocab_list(lecture_url)
        
        ser_vocab_list = VocabListSerializer(vocab_list)
        
        return Response(ser_vocab_list.data, status = s.HTTP_200_OK)