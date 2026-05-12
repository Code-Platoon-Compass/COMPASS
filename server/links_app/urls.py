from django.urls import path
from .views import LinkListView, LinkDetailView
 
urlpatterns = [
    path('', LinkListView.as_view(), name='link-list'),
    path('<uuid:link_id>/', LinkDetailView.as_view(), name='link-detail'),
]
 