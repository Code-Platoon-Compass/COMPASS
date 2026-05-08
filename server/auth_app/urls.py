from django.urls import path
from .views import OneInstructorView

urlpatterns = [
    path('instructors/', OneInstructorView.as_view(), name='auth-instructor')
]