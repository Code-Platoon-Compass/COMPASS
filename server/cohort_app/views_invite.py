from django.conf import settings
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import Cohort

class CohortInviteLinkView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, cohort_id):
        cohort = get_object_or_404(Cohort, id=cohort_id)

        base_url = getattr(
            settings,
            "COMPASS_INVITE_BASE_URL",
            "https://compass.codeplatoon.org/join"
        )

        invite_url = f"{base_url}/{cohort.invite_code}"

        return Response(
            {
                "cohort_id": str(cohort.id),
                "invite_code": cohort.invite_code,
                "invite_url": invite_url,
            },
            status=status.HTTP_200_OK,
        )
