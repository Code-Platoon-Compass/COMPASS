from rest_framework.serializers import ModelSerializer
from .models import DailyLink, ResourceLink

class DailyLinkSerializer(ModelSerializer):    
    class Meta:
        model = DailyLink
        fields = ['url', 'label', 'cohort']