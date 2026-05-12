from rest_framework.serializers import ModelSerializer
from .models import Cohort, DailyLink, ResourceLink, ValidEmail

class CohortSerializer(ModelSerializer):
    class Meta:
        model = Cohort
        fields = '__all__'

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