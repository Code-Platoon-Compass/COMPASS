from rest_framework.serializers import ModelSerializer
from .models import DailyLink, ResourceLink, ValidEmail

class DailyLinkSerializer(ModelSerializer):    
    class Meta:
        model = DailyLink
        fields = '__all__'
        
class ResourceLinkSerializer(ModelSerializer):    
    class Meta:
        model = ResourceLink
        fields = '__all__'

class ValidEmailSerializer(ModelSerializer):
    class Meta:
        model = ValidEmail
        fields = '__all__'