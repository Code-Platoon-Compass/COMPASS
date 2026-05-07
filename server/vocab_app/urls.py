from django.urls import include, path
from .views import VocabListView

urlpatterns = [
    path('', VocabListView.as_view(), name='vocab-list')
]