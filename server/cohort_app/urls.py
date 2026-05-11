from django.urls import path
from .views import AllDailyLinksView, OneDailyLinkView, AllResourceLinksView, OneResourceLinkView, AllValidEmailsView, OneValidEmailView

urlpatterns = [
    path('<uuid:cohort_id>/daily-links/', AllDailyLinksView.as_view(), name='all-daily-links'),
    path('<uuid:cohort_id>/daily-links/<uuid:link_id>/', OneDailyLinkView.as_view(), name='daily-link'),
    path('<uuid:cohort_id>/resource-links/', AllResourceLinksView.as_view(), name='all-resource-links'),
    path('<uuid:cohort_id>/resource-links/<uuid:link_id>/', OneResourceLinkView.as_view(), name='resource-link'),
    path('<uuid:cohort_id>/emails/', AllValidEmailsView.as_view(), name='all-valid-emails'),
    path('<uuid:cohort_id>/emails/<uuid:email_id>/', OneValidEmailView.as_view(), name='one-valid-email'),
]