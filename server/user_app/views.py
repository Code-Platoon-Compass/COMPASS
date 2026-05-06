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
from datetime import timedelta, datetime
from google.oauth2 import id_token
from google.auth.transport import requests
from django.db import transaction
from django.conf import settings
from django.core import signing
from urllib.parse import urlencode



class CreateStudentView(APIView):
    authentication_classes = []
    permission_classes = []
    pass
        





 