from django.shortcuts import render
from .models import DailyLink
from .serializers import DailyLinkSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as s
from django.shortcuts import get_object_or_404, get_list_or_404
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from uuid import UUID

# Create your views here.
validate = URLValidator()

class AllDailyLinksView(APIView):
    def get(self, request, cohort_id):
        links = get_list_or_404(DailyLink, cohort_id=cohort_id)
        serialized_links = DailyLinkSerializer(links, many=True)
        return Response(serialized_links.data, status=s.HTTP_200_OK)
    
    def post(self, request, cohort_id):
        try:
            validate(request.data["url"])
            dailylink_data = {
                "url": request.data["url"],
                "label": request.data["label"],
                "cohort_id": UUID(cohort_id)}
            return Response(dailylink_data, status=s.HTTP_200_OK)
            new_daily_link = DailyLinkSerializer(data=dailylink_data)
            if new_daily_link.is_valid():
                new_daily_link.save()
                return Response(new_daily_link.data, status=s.HTTP_201_CREATED)
            else:
                return Response(new_daily_link.errors, status=s.HTTP_400_BAD_REQUEST)
        except ValidationError as e:
            return Response(e.message, status=s.HTTP_400_BAD_REQUEST)

class OneDailyLinkView(APIView):
    def put(self, request, cohort_id, link_id):
        try:
            if request.data.get("url", None):
                validate(request.data.url)
            updated_daily_link = DailyLinkSerializer(
                get_object_or_404(DailyLink, id=link_id),
                data=request.data, partial=True)
            if updated_daily_link.is_valid():
                updated_daily_link.save()
                return Response(updated_daily_link.data, status=s.HTTP_200_OK)
            else:
                return Response(updated_daily_link.errors, status=s.HTTP_400_BAD_REQUEST)
        except ValidationError as e:
            return Response(e.message, status=s.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, cohort_id, link_id):
        daily_link = get_object_or_404(id=link_id)
        daily_link.delete()
        return Response(f"{link_id} has been deleted", status=s.HTTP_200_OK)
        