from django.shortcuts import redirect
from django.contrib.auth import authenticate
from COMPASS.server.auth_app.utilities import CookieAuthentication
from .models import User
from rest_framework import status as s
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from datetime import timedelta, datetime
from google.oauth2 import id_token
from google.auth.transport import requests
from django.conf import settings
from urllib.parse import urlencode

def generate_cookie_time(days=0, minutes=22):
    cookie_life = datetime.utcnow() + timedelta(days=days, minutes=minutes)
    format_time = cookie_life.strftime("%a, %d-%b-%Y %H:%M:%S GMT")
    return format_time

class RefreshAccessToken(APIView):
    authentication_classes = []
    permission_classes = []
    
    def post(self, request):
        refresh_token = request.COOKIES.get('refresh_token')
        
        if not refresh_token:
            return Response({'error': 'No token provided'}, status=s.HTTP_401_UNAUTHORIZED)
        
        try:
            token = RefreshToken(refresh_token)
            new_access_token = str(token.access_token)
            new_refresh_token = str(token)
            
            response = Response({'access_token': new_access_token}, status=s.HTTP_200_OK)
            
            response.set_cookie(
                key='access',
                value=new_access_token,
                httponly=True,
                secure=True,
                samesite='Lax',
                expires=generate_cookie_time(minutes=22)
            )
            response.set_cookie(
                key='refresh',
                value=new_refresh_token,
                httponly=True,
                secure=True,
                samesite='Lax',
                expires=generate_cookie_time(days=7)
            )
            return response
        except (TokenError, InvalidToken) as e:
            return Response(str(e), status=s.HTTP_401_UNAUTHORIZED)

class CreateUserView(APIView):
    authentication_classes = []
    permission_classes = []
    pass

class LoginView(APIView):
    authentication_classes = []
    permission_classes = []
    pass

class LogoutView(APIView):
    authentication_classes = []
    permission_classes = []
    pass

class GoogleOAuthView(APIView):
    authentication_classes = []
    permission_classes = []
    
    def get(self, request):
        params = {
            'client_id': settings.GOOGLE_CLIENT_ID,
            'redirect_uri': settings.GOOGLE_REDIRECT_URI,
            'response_type': 'code',
            'scope': 'openid email profile',
            'access_type': 'offline',
            'prompt': 'consent'
        }
        google_auth_url = f"https://accounts.google.com/o/oauth2/v2/auth?{urlencode(params)}"
        return redirect(google_auth_url)

