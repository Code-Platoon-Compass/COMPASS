from django.shortcuts import redirect
from django.contrib.auth import authenticate

from COMPASS.server.auth_app.utilities import CookieAuthentication
from .models import Student
from rest_framework import status as s
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from datetinme import timedelta, datetime
from django.db import transaction
from django.conf import settings
from django.core import signing
from urllib.parse import urlencode

def generate_cookie_time(days=0, minutes=22):
    cookie_life = datetime.utcnow() + timedelta(days=days, minutes=minutes)
    format_time = cookie_life.strftime("%a, %d-%b-%Y %H:%M:%S GMT")
    return format_time



class CreateStudentView(APIView):
    authentication_classes = [CookieAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        student = request.user
        data = request.data
        data['cohort'] = student.cohort.id
        new_student = Student.objects.create(**data)
        
        try:
            new_student.full_clean()
            new_student.save()
        except Exception as e:
            return Response({'error': str(e)}, status=s.HTTP_400_BAD_REQUEST)
        return Response({'message': 'Student created successfully'}, status=s.HTTP_201_CREATED)
        

class LoginView(APIView):
    pass

class LogoutView(APIView):
    pass

class GoogleOAuthView(APIView):
    pass

