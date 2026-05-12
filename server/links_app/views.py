from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as s
from .models import Link
from .serializers import LinkSerializer
 
 
class LinkListView(APIView):
    """
    API view for listing and creating links.
 
    Endpoints:
        GET    api/v1/links/  - List all links
        POST   api/v1/links/  - Create a new link
 
    Authentication is enforced globally via DEFAULT_PERMISSION_CLASSES.
    """
 
    def get(self, request):
        """
        Return all links, newest first.
        """
        links = Link.objects.all()
        serializer = LinkSerializer(links, many=True)
        return Response(serializer.data, status=s.HTTP_200_OK)
 
    def post(self, request):
        """
        Create a new link.
 
        Request body:
            {
                "label": "Course Syllabus",
                "url":   "https://example.com/syllabus"
            }
        """
        serializer = LinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=s.HTTP_201_CREATED)
        return Response(serializer.errors, status=s.HTTP_400_BAD_REQUEST)
 
 
class LinkDetailView(APIView):
    """
    API view for retrieving, updating, and deleting a single link.
 
    Endpoints:
        GET    api/v1/links/<id>/  - Retrieve one link
        PUT    api/v1/links/<id>/  - Update a link
        DELETE api/v1/links/<id>/  - Delete a link
    """
 
    def _get_link(self, link_id):
        return Link.objects.filter(id=link_id).first()
 
    def get(self, request, link_id):
        link = self._get_link(link_id)
        if not link:
            return Response({"error": "Link not found"}, status=s.HTTP_404_NOT_FOUND)
        return Response(LinkSerializer(link).data, status=s.HTTP_200_OK)
 
    def put(self, request, link_id):
        link = self._get_link(link_id)
        if not link:
            return Response({"error": "Link not found"}, status=s.HTTP_404_NOT_FOUND)
        serializer = LinkSerializer(link, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=s.HTTP_200_OK)
        return Response(serializer.errors, status=s.HTTP_400_BAD_REQUEST)
 
    def delete(self, request, link_id):
        link = self._get_link(link_id)
        if not link:
            return Response({"error": "Link not found"}, status=s.HTTP_404_NOT_FOUND)
        link.delete()
        return Response({"message": "Link deleted successfully"}, status=s.HTTP_200_OK)