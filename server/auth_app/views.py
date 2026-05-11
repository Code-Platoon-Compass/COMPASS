from rest_framework import status as s
from rest_framework.views import APIView
from rest_framework.response import Response
import logging
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from datetime import timedelta, datetime
from google.oauth2 import id_token
from google.auth.transport import requests
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import transaction
from cohort_app.models import Cohort, ValidEmail
from .models import Instructor, Student
from rest_framework.permissions import IsAuthenticated
from .serializers import InstructorSerializer
from secrets import token_hex

logger = logging.getLogger(__name__)

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

def auth_api_key(request):
    api_key = request.headers.get("X-Api-Key", "")
    return len(Instructor.objects.filter(api_key=api_key)) == 1

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


class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response(
            {
                'email': user.email,
                'name': f"{user.first_name} {user.last_name}".strip(),
            },
            status=s.HTTP_200_OK,
        )

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
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        token = request.data.get('token')
        invite_code = (request.data.get('invite_code') or '').strip()

        if not token:
            return Response({'error': 'No token provided'}, status=s.HTTP_400_BAD_REQUEST)
        
        try:
            id_info = id_token.verify_oauth2_token(token, requests.Request(), settings.GOOGLE_CLIENT_ID)
            email = id_info.get('email')
            name = id_info.get('name')
            google_id = id_info.get('sub')

            if not email:
                return Response({'error': 'Google account email is required'}, status=s.HTTP_400_BAD_REQUEST)

            if not google_id:
                return Response({'error': 'Google account identifier is required'}, status=s.HTTP_400_BAD_REQUEST)

            normalized_email = email.strip().lower()
            cohort = None

            existing_student = Student.objects.select_related('cohort').filter(google_id=google_id).first()

            # Returning users can sign in without re-entering the cohort invite code.
            if existing_student:
                cohort = existing_student.cohort
                if cohort is None:
                    return Response({'error': 'Student is not assigned to a cohort'}, status=s.HTTP_403_FORBIDDEN)
            else:
                if not invite_code:
                    return Response({'error': 'Invite code is required for first sign in'}, status=s.HTTP_400_BAD_REQUEST)

                try:
                    cohort = Cohort.objects.get(invite_code=invite_code)
                except Cohort.DoesNotExist:
                    return Response({'error': 'Invalid invite code'}, status=s.HTTP_403_FORBIDDEN)

                is_allowed_email = ValidEmail.objects.filter(
                    cohort=cohort,
                    email__iexact=normalized_email,
                ).exists()

                if not is_allowed_email:
                    return Response({'error': 'Google email is not approved for this cohort'}, status=s.HTTP_403_FORBIDDEN)

            User = get_user_model()

            # Create account only after Google verification and allowlist checks pass.
            with transaction.atomic():
                user, created = User.objects.get_or_create(
                    email=normalized_email,
                    defaults={
                        'username': normalized_email,
                    },
                )

                if name:
                    name_parts = name.split(' ', 1)
                    first_name = name_parts[0]
                    last_name = name_parts[1] if len(name_parts) > 1 else ''

                    if user.first_name != first_name or user.last_name != last_name:
                        user.first_name = first_name
                        user.last_name = last_name
                        user.save(update_fields=['first_name', 'last_name'])

                if existing_student:
                    student_updates = []

                    if existing_student.email != normalized_email:
                        existing_student.email = normalized_email
                        student_updates.append('email')

                    expected_name = name or normalized_email
                    if existing_student.name != expected_name:
                        existing_student.name = expected_name
                        student_updates.append('name')

                    if student_updates:
                        existing_student.save(update_fields=student_updates)
                else:
                    Student.objects.create(
                        google_id=google_id,
                        cohort=cohort,
                        name=name or normalized_email,
                        email=normalized_email,
                    )

            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            response_data = {
                'email': user.email,
                'name': f"{user.first_name} {user.last_name}".strip(),
                'created': created,
                'cohort_id': str(cohort.id),
            }
            response = Response(response_data, status=s.HTTP_200_OK)
            return set_token_cookies(response, access_token, refresh_token)
        except ValueError as e:
            import traceback
            logger.error(f'Google token verification failed: {str(e)}\n{traceback.format_exc()}')
            return Response({'error': 'Invalid token'}, status=s.HTTP_400_BAD_REQUEST)

class OneInstructorView(APIView):
    def post(self, request):
        # TODO: link to superuser, see discussion
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