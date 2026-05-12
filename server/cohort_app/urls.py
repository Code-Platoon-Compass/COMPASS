from django.urls import path
from .views import *
from .views_invite import CohortInviteLinkView

urlpatterns = [
    # Invite link endpoint
    path(
        '<uuid:cohort_id>/invite-link/',
        CohortInviteLinkView.as_view(),
        name='cohort-invite-link'
    ),

    # Daily links
    path(
        '<uuid:cohort_id>/daily-link/',
        AllDailyLinksView.as_view(),
        name='all-daily-links'
    ),
    path(
        '<uuid:cohort_id>/daily-link/<uuid:link_id>/',
        OneDailyLinkView.as_view(),
        name='daily-link'
    ),

    # Resource links
    path(
        '<uuid:cohort_id>/resource-link/',
        AllResourceLinksView.as_view(),
        name='all-resource-links'
    ),
    path(
        '<uuid:cohort_id>/resource-links/<uuid:link_id>/',
        OneResourceLinkView.as_view(),
        name='resource-link'
    ),

    # Valid emails
    path(
        '<uuid:cohort_id>/emails/',
        AllValidEmailsView.as_view(),
        name='all-valid-emails'
    ),
    path(
        '<uuid:cohort_id>/emails/<uuid:email_id>/',
        OneValidEmailView.as_view(),
        name='one-valid-email'
    ),
    path('', CohortView.as_view(), name='one-cohort')
]
