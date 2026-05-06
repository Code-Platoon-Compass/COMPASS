from django.urls import path
from .views import AllDailyLinks, DailyLink

urlpatterns = [
    path('<int:cohort_id>/daily_links', AllDailyLinks.as_view(), name='all-daily-links'),
    path('<int:cohort_id>/daily_links/<int:link_id>', DailyLink.as_view(), name='daily-link')
]