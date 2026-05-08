from unittest.mock import patch

from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from cohort_app.models import Cohort, ValidEmail


class GoogleAuthFlowTests(TestCase):
	def setUp(self):
		self.client = APIClient()
		self.google_auth_url = reverse('google_oauth')
		self.invite_code = 'TEST-INVITE-123'
		self.allowed_email = 'kamivision@gmail.com'
		self.cohort = Cohort.objects.create(name='Test Cohort', invite_code=self.invite_code)
		ValidEmail.objects.create(cohort=self.cohort, email=self.allowed_email)

	@patch('auth_app.views.id_token.verify_oauth2_token')
	def test_google_auth_success_sets_cookies_and_creates_user(self, mock_verify):
		mock_verify.return_value = {
			'email': self.allowed_email,
			'name': 'Kami Vision',
		}

		payload = {
			'token': 'fake-google-token',
			'invite_code': self.invite_code,
		}

		response = self.client.post(self.google_auth_url, payload, format='json')

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data['email'], self.allowed_email)
		self.assertTrue(response.data['created'])
		self.assertIn(settings.JWT_ACCESS_COOKIE, response.cookies)
		self.assertIn(settings.JWT_REFRESH_COOKIE, response.cookies)

		User = get_user_model()
		self.assertTrue(User.objects.filter(email=self.allowed_email).exists())

	@patch('auth_app.views.id_token.verify_oauth2_token')
	def test_google_auth_invalid_invite_code_returns_403(self, mock_verify):
		mock_verify.return_value = {
			'email': self.allowed_email,
			'name': 'Kami Vision',
		}

		payload = {
			'token': 'fake-google-token',
			'invite_code': 'WRONG-CODE',
		}

		response = self.client.post(self.google_auth_url, payload, format='json')

		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
		self.assertEqual(response.data['error'], 'Invalid invite code')

	@patch('auth_app.views.id_token.verify_oauth2_token')
	def test_google_auth_email_not_allowlisted_returns_403(self, mock_verify):
		mock_verify.return_value = {
			'email': 'not-allowed@example.com',
			'name': 'Other Student',
		}

		payload = {
			'token': 'fake-google-token',
			'invite_code': self.invite_code,
		}

		response = self.client.post(self.google_auth_url, payload, format='json')

		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
		self.assertEqual(response.data['error'], 'Google email is not approved for this cohort')

	@patch('auth_app.views.id_token.verify_oauth2_token')
	def test_google_auth_missing_token_returns_400(self, mock_verify):
		payload = {
			'invite_code': self.invite_code,
		}

		response = self.client.post(self.google_auth_url, payload, format='json')

		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
		self.assertEqual(response.data['error'], 'No token provided')
		mock_verify.assert_not_called()

	@patch('auth_app.views.id_token.verify_oauth2_token')
	def test_google_auth_missing_invite_code_returns_400(self, mock_verify):
		payload = {
			'token': 'fake-google-token',
		}

		response = self.client.post(self.google_auth_url, payload, format='json')

		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
		self.assertEqual(response.data['error'], 'Invite code is required')
		mock_verify.assert_not_called()


class SessionCookieFlowTests(TestCase):
	def setUp(self):
		self.client = APIClient()
		self.refresh_url = reverse('refresh')
		self.logout_url = reverse('logout')

		User = get_user_model()
		self.user = User.objects.create_user(
			email='kamivision@gmail.com',
			username='kamivision@gmail.com',
			password='testpass123'
		)

	def test_refresh_success_issues_new_cookie_tokens(self):
		refresh = RefreshToken.for_user(self.user)
		self.client.cookies[settings.JWT_REFRESH_COOKIE] = str(refresh)

		response = self.client.post(self.refresh_url, {}, format='json')

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertIn(settings.JWT_ACCESS_COOKIE, response.cookies)
		self.assertIn(settings.JWT_REFRESH_COOKIE, response.cookies)

	def test_refresh_missing_cookie_returns_401(self):
		response = self.client.post(self.refresh_url, {}, format='json')

		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
		self.assertEqual(response.data['error'], 'No token provided')

	def test_logout_clears_auth_cookies(self):
		self.client.cookies[settings.JWT_ACCESS_COOKIE] = 'old-access'
		self.client.cookies[settings.JWT_REFRESH_COOKIE] = 'old-refresh'

		response = self.client.post(self.logout_url, {}, format='json')

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertIn(settings.JWT_ACCESS_COOKIE, response.cookies)
		self.assertIn(settings.JWT_REFRESH_COOKIE, response.cookies)
		self.assertEqual(response.cookies[settings.JWT_ACCESS_COOKIE].value, '')
		self.assertEqual(response.cookies[settings.JWT_REFRESH_COOKIE].value, '')
