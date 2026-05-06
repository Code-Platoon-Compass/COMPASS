from django.urls import path
from .views import *

urlpatterns = [
    path('create-student/', CreateStudentView.as_view(), name='create_student'),
    
]