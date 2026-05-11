from rest_framework.serializers import ModelSerializer
from .models import Instructor

class InstructorSerializer(ModelSerializer):
    class Meta:
        model = Instructor
        fields = ['name', 'email', 'api_key']