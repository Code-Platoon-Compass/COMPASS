from django.conf import settings
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from cohort_app.models import Cohort
from auth_app.models import User


class CohortInviteLinkViewTests(APITestCase):
    def setUp(self):
        # Create a user and authenticate them
        self.user = User.objects.create_user(
            username="instructor",
            email="instructor@example.com",
            password="testpassword",
        )

        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        # Create a cohort with an invite code
        self.cohort = Cohort.objects.create(
            name="Test Cohort",
            invite_code="TESTCODE123",
        )

        # Base URL from settings
        self.base_url = getattr(
            settings,
            "COMPASS_INVITE_BASE_URL",
            "https://compass.codeplatoon.org/join",
        )

    def test_get_invite_link_success(self):
        url = f"/api/v1/cohorts/{self.cohort.id}/invite-link/"

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["cohort_id"], str(self.cohort.id))
        self.assertEqual(response.data["invite_code"], self.cohort.invite_code)
        self.assertEqual(
            response.data["invite_url"],
            f"{self.base_url}/{self.cohort.invite_code}",
        )

    def test_get_invite_link_invalid_cohort_returns_404(self):
        url = "/api/v1/cohorts/00000000-0000-0000-0000-000000000000/invite-link/"

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


