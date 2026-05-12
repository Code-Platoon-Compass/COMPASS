from django.urls import path
from .views import OneInstructorView

urlpatterns = [
    path('create/', OneInstructorView.as_view(), name='auth-instructor'),
]