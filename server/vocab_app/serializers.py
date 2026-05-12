from rest_framework import serializers
from .models import VocabItem, VocabList

class VocabItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = VocabItem
        fields = ['term', 'definition'] 

class VocabListSerializer(serializers.ModelSerializer):
    items = VocabItemSerializer(many=True, read_only=True)

    class Meta:
        model = VocabList
        fields = ['lecture_url', 'items']