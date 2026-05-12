from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from auth_app.models import Instructor


class APIKeyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        api_key = request.headers.get("X-API-Key")

        if not api_key:
            raise AuthenticationFailed("API key missing")

        try:
            instructor = Instructor.objects.get(api_key=api_key)
        except Instructor.DoesNotExist:
            raise AuthenticationFailed("Invalid API key")

        return (instructor, None)
