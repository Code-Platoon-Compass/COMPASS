from django.shortcuts import render
from instructor_app.models import Instructor
from .models import DailyLink, ResourceLink, ValidEmail
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as s
from django.shortcuts import get_object_or_404, get_list_or_404
from secrets import token_urlsafe

# Create your views here.
def auth_api_key(request):
    api_key = request.headers.get("X-Api-Key", "")
    return len(Instructor.objects.filter(api_key=api_key)) == 1

# (request:Json request body, cohort_id:str) -> List[dict] for ResourceLink serializer
def multiple_resource_links_data(request, cohort_id:str):
    try:
        validresource_data = []
        for resource_dict in request.data['resource_links']:
            # only adds new resource urls (combines lists)
            if len(ResourceLink.objects.filter(cohort_id=cohort_id, url=resource_dict['url'])) == 0:
                validresource_data.append({
                    "url": resource_dict['url'],
                    "label": resource_dict['label'],
                    "cohort": cohort_id})
        return validresource_data
    except:
        return []

# (request:Json request body, cohort_id:str) -> List[dict] for ResourceLink serializer
def multiple_daily_links_data(request, cohort_id:str):
    try:
        valid_daily_data = []
        for daily_dict in request.data['daily_links']:
            # only add new daily links (combines lists)
            if len(DailyLink.objects.filter(cohort_id=cohort_id, url=daily_dict['url'])) == 0:
                valid_daily_data.append({
                    "url": daily_dict['url'],
                    "label": daily_dict['label'],
                    "cohort": cohort_id
                })
        return valid_daily_data
    except:
        return []

# (request:Json request body, cohort_id:str) -> List[dict] for ValidEmail serializer
def multiple_emails(request, cohort_id:str):
    try:
        validemail_data = []
        for email in request.data['email']:
            # only adds new emails (combines lists)
            if len(ValidEmail.objects.filter(cohort_id=cohort_id, email=email)) == 0:
                validemail_data.append({
                    "email": email,
                    "cohort": cohort_id})
        return validemail_data  
    except:
        return []

class AllDailyLinksView(APIView):
    authentication_classes = []
    permission_classes = []
    
    def get(self, request, cohort_id):
        links = get_list_or_404(DailyLink, cohort_id=cohort_id)
        serialized_links = DailyLinkSerializer(links, many=True)
        return Response(serialized_links.data, status=s.HTTP_200_OK)
    
    def post(self, request, cohort_id):
        if auth_api_key(request):
            data = multiple_daily_links_data(request, cohort_id)
            if not data:
                return Response("No links were given", status=s.HTTP_400_BAD_REQUEST)
            new_daily_link = DailyLinkSerializer(data=data, many=True)
            if new_daily_link.is_valid():
                new_daily_link.save()
                return Response(new_daily_link.data, status=s.HTTP_201_CREATED)
            else:
                return Response(new_daily_link.errors, status=s.HTTP_400_BAD_REQUEST)
        else:
            return Response("Unable to authorize user", status=s.HTTP_403_FORBIDDEN)

class OneDailyLinkView(APIView):
    authentication_classes = []
    permission_classes = []

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
    authentication_classes = []
    permission_classes = []

    def get(self, request, cohort_id):
        links = get_list_or_404(ResourceLink, cohort_id=cohort_id)
        serialized_links = ResourceLinkSerializer(links, many=True)
        return Response(serialized_links.data, status=s.HTTP_200_OK)
        
    # resource in a list of tuples(url, label)
    def post(self, request, cohort_id):
        if auth_api_key(request):
            data = multiple_resource_links_data(request, cohort_id)
            if not data:
                return Response("No links were given", status=s.HTTP_400_BAD_REQUEST)
            new_resource_links = ResourceLinkSerializer(data=data, many=True)
            if new_resource_links.is_valid():
                new_resource_links.save()
                return Response(new_resource_links.data, status=s.HTTP_201_CREATED)
            else:
                return Response(new_resource_links.errors, status=s.HTTP_400_BAD_REQUEST)
        else:
            return Response("Unable to authorize user", status=s.HTTP_403_FORBIDDEN)

class OneResourceLinkView(APIView):
    authentication_classes = []
    permission_classes = []

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
    authentication_classes = []
    permission_classes = []

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
            data = multiple_emails(request, cohort_id)
            if not data:
                return Response("No emails were given", status=s.HTTP_400_BAD_REQUEST)
            new_validemail = ValidEmailSerializer(data=data, many=True)
            if new_validemail.is_valid():
                new_validemail.save()
                return Response(new_validemail.data, status=s.HTTP_201_CREATED)
            else:
                return Response(new_validemail.errors, status=s.HTTP_400_BAD_REQUEST)
        else:
            return Response("Unable to authorize user", status=s.HTTP_403_FORBIDDEN)

class OneValidEmailView(APIView):
    authentication_classes = []
    permission_classes = []

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

class CohortView(APIView):
    authentication_classes = []
    permission_classes = []
    
    def get(self, request):
        if auth_api_key(request):
            cohorts = get_list_or_404(Cohort)
            serialized_cohorts = CohortSerializer(cohorts, many=True)
            return Response(serialized_cohorts.data, status=s.HTTP_200_OK)
        else:
            return Response("Unable to authorize user", status=s.HTTP_403_FORBIDDEN)

    def post(self, request):
        if auth_api_key(request):
            cohort_data = {
                'name': request.data['name'],
                'invite_code': token_urlsafe(10)
            }
            new_cohort = CohortSerializer(data=cohort_data)
            if new_cohort.is_valid():
                new_cohort.save()
                ret = new_cohort.data.copy()
                new_id = new_cohort.data['id']
                # check to see if there's any daily links, resource links, or email lists
                daily_link_data = multiple_daily_links_data(request, new_id)
                if daily_link_data:
                    new_dailies = DailyLinkSerializer(data=daily_link_data, many=True)
                    if new_dailies.is_valid():
                        new_dailies.save()
                        ret['daily'] = True
                    else:
                        ret['daily'] = new_dailies.errors
                resource_link_data = multiple_resource_links_data(request, new_id)
                if resource_link_data:
                    new_resources = ResourceLinkSerializer(data=resource_link_data, many=True)
                    if new_resources.is_valid():
                        new_resources.save()
                        ret['resource'] = True
                    else:
                        ret['resource'] = new_resources.errors
                email_data = multiple_emails(request, new_id)
                if email_data:
                    new_emails = ValidEmailSerializer(data=email_data, many=True)
                    if new_emails.is_valid():
                        new_emails.save()
                        ret['email'] = True
                    else:
                        ret['email'] = new_emails.errors
                return Response(ret, status=s.HTTP_201_CREATED)
            else:
                return Response(new_cohort.errors, status=s.HTTP_400_BAD_REQUEST)
        else:
            return Response("Unable to authorize user", status=s.HTTP_403_FORBIDDEN)