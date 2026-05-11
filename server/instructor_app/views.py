from rest_framework import status as s
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Instructor
from .serializers import InstructorSerializer
from secrets import token_hex

# Create your views here.
def auth_api_key(request):
    api_key = request.headers.get("X-Api-Key", "")
    return len(Instructor.objects.filter(api_key=api_key)) == 1

class OneInstructorView(APIView):
    authentication_classes = []
    permission_classes = []
    
    def post(self, request):
        if auth_api_key(request):
            data = {
                "name": request.data['name'],
                "email": request.data['email'],
                "api_key": token_hex(16)
            }
            new_instructor = InstructorSerializer(data=data)
            if new_instructor.is_valid():
                new_instructor.save()
                return Response(new_instructor.data, status=s.HTTP_201_CREATED)
            else:
                return Response(new_instructor.errors, status=s.HTTP_400_BAD_REQUEST)
        else:
            return Response("Unable to authorize user", status=s.HTTP_403_FORBIDDEN)