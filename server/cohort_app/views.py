from django.shortcuts import render
from instructor_app.models import Instructor
from .models import DailyLink, ResourceLink, ValidEmail
from .serializers import DailyLinkSerializer, ResourceLinkSerializer, ValidEmailSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as s
from django.shortcuts import get_object_or_404, get_list_or_404

# Create your views here.
authentication_classes = []
permission_classes = []

def auth_api_key(request):
    api_key = request.headers.get("X-Api-Key", "")
    return len(Instructor.objects.filter(api_key=api_key)) == 1

class AllDailyLinksView(APIView):
    
    def get(self, request, cohort_id):
        links = get_list_or_404(DailyLink, cohort_id=cohort_id)
        serialized_links = DailyLinkSerializer(links, many=True)
        return Response(serialized_links.data, status=s.HTTP_200_OK)
    
    def post(self, request, cohort_id):
        if auth_api_key(request):
            dailylink_data = {
                "url": request.data["url"],
                "label": request.data["label"],
                "cohort": cohort_id}
            new_daily_link = DailyLinkSerializer(data=dailylink_data)
            if new_daily_link.is_valid():
                new_daily_link.save()
                return Response(new_daily_link.data, status=s.HTTP_201_CREATED)
            else:
                return Response(new_daily_link.errors, status=s.HTTP_400_BAD_REQUEST)
        else:
            return Response("Unable to authorize user", status=s.HTTP_403_FORBIDDEN)

class OneDailyLinkView(APIView):
    
    def put(self, request, cohort_id, link_id):
        if auth_api_key(request):
            updated_daily_link = DailyLinkSerializer(
                get_object_or_404(DailyLink, id=link_id),
                data=request.data, 
                partial=True)
            if updated_daily_link.is_valid():
                updated_daily_link.save()
                return Response(updated_daily_link.data, status=s.HTTP_200_OK)
            else:
                return Response(updated_daily_link.errors, status=s.HTTP_400_BAD_REQUEST)
        else:
            return Response("Unable to authorize user", status=s.HTTP_403_FORBIDDEN)
        
    
    def delete(self, request, cohort_id, link_id):
        if auth_api_key(request):
            daily_link = get_object_or_404(DailyLink, id=link_id)
            ret_str = f"{daily_link.label} ({daily_link.url})"
            daily_link.delete()
            return Response(f"{ret_str} has been deleted", status=s.HTTP_200_OK)
        else:
            return Response("Unable to authorize user", status=s.HTTP_403_FORBIDDEN)
        
class AllResourceLinksView(APIView):
    
    def get(self, request, cohort_id):
        links = get_list_or_404(ResourceLink, cohort_id=cohort_id)
        serialized_links = ResourceLinkSerializer(links, many=True)
        return Response(serialized_links.data, status=s.HTTP_200_OK)
        
    def post(self, request, cohort_id):
        if auth_api_key(request):
            resourcelink_data = {
                "url": request.data["url"],
                "label": request.data["label"],
                "cohort": cohort_id}
            new_resource_link = ResourceLinkSerializer(data=resourcelink_data)
            if new_resource_link.is_valid():
                new_resource_link.save()
                return Response(new_resource_link.data, status=s.HTTP_201_CREATED)
            else:
                return Response(new_resource_link.errors, status=s.HTTP_400_BAD_REQUEST)
        else:
            return Response("Unable to authorize user", status=s.HTTP_403_FORBIDDEN)

class OneResourceLinkView(APIView):
    
    def put(self, request, cohort_id, link_id):
        if auth_api_key(request):
            updated_resource_link = ResourceLinkSerializer(
                get_object_or_404(ResourceLink, id=link_id),
                    data=request.data, 
                    partial=True)
            if updated_resource_link.is_valid():
                updated_resource_link.save()
                return Response(updated_resource_link.data, status=s.HTTP_200_OK)
            else:
                return Response(updated_resource_link.errors, status=s.HTTP_400_BAD_REQUEST)
        else:
            return Response("Unable to authorize user", status=s.HTTP_403_FORBIDDEN)
        
    
    def delete(self, request, cohort_id, link_id):
        if auth_api_key(request):
            resource_link = get_object_or_404(ResourceLink, id=link_id)
            ret_str = f"{resource_link.label} ({resource_link.url})"
            resource_link.delete()
            return Response(f"{ret_str} has been deleted", status=s.HTTP_200_OK)
        else:
            return Response("Unable to authorize user", status=s.HTTP_403_FORBIDDEN)

class AllValidEmailsView(APIView):
    
    def get(self, request, cohort_id):
        if auth_api_key(request):
            links = get_list_or_404(ValidEmail, cohort_id=cohort_id)
            serialized_emails = ValidEmailSerializer(links, many=True)
            return Response(serialized_emails.data, status=s.HTTP_200_OK)
        else:
            return Response("Unable to authorize user", status=s.HTTP_403_FORBIDDEN)
        
    def post(self, request, cohort_id):
        # test bulk support, assume "email" request field is a list
        if auth_api_key(request):
            validemail_data = []
            for email in request.data['email']:
                # only adds new emails, so can combine lists this way
                if len(ValidEmail.objects.filter(cohort_id=cohort_id, email=email)) == 0:
                    validemail_data.append({
                        "email": email,
                        "cohort": cohort_id})
            new_validemail = ValidEmailSerializer(data=validemail_data, many=True)
            if new_validemail.is_valid():
                new_validemail.save()
                return Response(new_validemail.data, status=s.HTTP_201_CREATED)
            else:
                return Response(new_validemail.errors, status=s.HTTP_400_BAD_REQUEST)
        else:
            return Response("Unable to authorize user", status=s.HTTP_403_FORBIDDEN)

class OneValidEmailView(APIView):
    
    # this put essentially only updates the email
    def put(self, request, cohort_id, email_id):
        if auth_api_key(request):
            updated_validemail = ValidEmailSerializer(
                get_object_or_404(ValidEmail, id=email_id),
                    data=request.data, 
                    partial=True)
            if updated_validemail.is_valid():
                updated_validemail.save()
                return Response(updated_validemail.data, status=s.HTTP_200_OK)
            else:
                return Response(updated_validemail.errors, status=s.HTTP_400_BAD_REQUEST)
        else:
            return Response("Unable to authorize user", status=s.HTTP_403_FORBIDDEN)
        
    
    def delete(self, request, cohort_id, email_id):
        if auth_api_key(request):
            valid_email = get_object_or_404(ValidEmail, id=email_id)
            ret_str = f"{valid_email.email}"
            valid_email.delete()
            return Response(f"{ret_str} has been deleted", status=s.HTTP_200_OK)
        else:
            return Response("Unable to authorize user", status=s.HTTP_403_FORBIDDEN)