from rest_framework.request import Request
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework import exceptions
from rest_framework_simplejwt.tokens import AuthUser, Token

class CookieAuthentication(JWTAuthentication):
    
    def get_auth_cookie(self, request):
        return request.COOKIES.get('access_token')
    
    def authenticate(self, request):
        access_token = self.get_auth_cookie(request)
        
        if not access_token:
            raise exceptions.AuthenticationFailed('No access token provided in cookies.')
        
        try:
            validated_token = self.get_validated_token(access_token)
            return self.get_user(validated_token), validated_token
        except TokenError as e:
            raise exceptions.AuthenticationFailed('Invalid token') from e

        