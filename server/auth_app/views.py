from rest_framework import status as s
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from datetime import timedelta, datetime
from google.oauth2 import id_token
from google.auth.transport import requests
from django.conf import settings

def generate_cookie_time(days=0, minutes=22):
    cookie_life = datetime.utcnow() + timedelta(days=days, minutes=minutes)
    format_time = cookie_life.strftime("%a, %d-%b-%Y %H:%M:%S GMT")
    return format_time


def set_token_cookies(response, access_token, refresh_token):
    response.set_cookie(
        key=settings.JWT_ACCESS_COOKIE,
        value=access_token,
        httponly=True,
        secure=True,
        samesite='Lax',
        expires=generate_cookie_time(minutes=22)
    )
    response.set_cookie(
        key=settings.JWT_REFRESH_COOKIE,
        value=refresh_token,
        httponly=True,
        secure=True,
        samesite='Lax',
        expires=generate_cookie_time(days=7)
    )
    return response


def clear_token_cookies(response):
    response.delete_cookie(settings.JWT_ACCESS_COOKIE, samesite='Lax')
    response.delete_cookie(settings.JWT_REFRESH_COOKIE, samesite='Lax')
    return response

class RefreshAccessToken(APIView):
    authentication_classes = []
    permission_classes = []
    
    def post(self, request):
        refresh_token = request.COOKIES.get(settings.JWT_REFRESH_COOKIE)
        
        if not refresh_token:
            return Response({'error': 'No token provided'}, status=s.HTTP_401_UNAUTHORIZED)
        
        try:
            token = RefreshToken(refresh_token)
            new_access_token = str(token.access_token)
            new_refresh_token = str(token)
            
            response = Response({'access_token': new_access_token}, status=s.HTTP_200_OK)
            return set_token_cookies(response, new_access_token, new_refresh_token)
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

    def post(self, request):
        response = Response({'message': 'Logged out successfully'}, status=s.HTTP_200_OK)
        return clear_token_cookies(response)

class GoogleOAuthView(APIView):
    pass

