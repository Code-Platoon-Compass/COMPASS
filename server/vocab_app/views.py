from .models import  VocabItem, VocabList
from .gemini_utils import get_vocab_list, generate_vocab_list
from rest_framework.response import Response
from rest_framework.views import APIView

class VocabListView(APIView):
    def post (self,request):
        lecture_url = self.request.data.get('lecture_url')
        
        if not lecture_url:
            return Response({"error": "lecture_url is required"}, status=400)
        
        vocab_list = get_vocab_list(lecture_url)
        
        if vocab_list:
            items = VocabItem.objects.filter(vocab_list_url=vocab_list.lecture_url)
            return Response({
                "lecture_url": vocab_list.lecture_url,
                "items": [{"term": item.term, "definition": item.definition} for item in items]
            })
        
        vocab_list = generate_vocab_list(lecture_url)
        
        items = VocabItem.objects.filter(vocab_list_url = vocab_list.lecture_url)
        
        return Response({
            "lecture_url": vocab_list.lecture_url,
            "items": [{"term": item.term, "definition": item.definition} for item in items]
        })