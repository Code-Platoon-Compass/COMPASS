from django.urls import path
from .views import AllDailyLinksView, OneDailyLinkView

urlpatterns = [
    path('<uuid:cohort_id>/daily-links/', AllDailyLinksView.as_view(), name='all-daily-links'),
    path('<uuid:cohort_id>/daily-links/<int:link_id>/', OneDailyLinkView.as_view(), name='daily-link')
]