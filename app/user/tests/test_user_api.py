from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status


CREATE_USER_URL = reverse("user:create")
TOKEN_URL = reverse("user:token")


def create_user(**params):
    return get_user_model().objects.create_user(**params)


class PublicUserApiTests(TestCase):
    """Test the users API (public)"""

    def setUp(self) -> None:
        self.client = APIClient()

    def test_create_valid_user_success(self) -> None:
        """Test creating user with valid payload is successful"""
        payload = {
            "email": "test@gawlowski.com.pl",
            "password": "password1234",
            "name": "Test API User"
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(**res.data)
        self.assertTrue(user.check_password(payload["password"]))
        self.assertNotIn("password", res.data)

    def test_user_exists(self) -> None:
        """Test creating user that already exists fails"""
        payload = {
            "email": "test@gawlowski.com.pl",
            "password": "password1234",
            "name": "Test API User"
        }
        create_user(**payload)

        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self) -> None:
        """Test that the password must be more than 12 characters"""
        payload = {
            "email": "test@gawlowski.com.pl",
            "password": "password",
            "name": "Test API User"
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(
            email=payload["email"]
        ).exists()
        self.assertFalse(user_exists)

    def test_create_token_for_api_user(self) -> None:
        """Test that a token is created for the API user"""
        payload = {
            "email": "test@gawlowski.com.pl",
            "password": "password1234",
            "name": "Test API User"
        }
        create_user(**payload)
        res = self.client.post(TOKEN_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIn("token", res.data)

    def test_create_token_invalid_credentials(self) -> None:
        """Test that token is not created if invalid credentials are given"""
        payload = {
            "email": "test@gawlowski.com.pl",
            "password": "password1234",
            "name": "Test API User"
        }
        create_user(**payload)
        payload["password"] = "invalidpassword"
        res = self.client.post(TOKEN_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn("token", res.data)

    def test_create_token_no_user(self) -> None:
        """Test that token is not created if user does not exist"""
        payload = {
            "email": "test@gawlowski.com.pl",
            "password": "password1234",
            "name": "Test API User"
        }
        res = self.client.post(TOKEN_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn("token", res.data)

    def test_create_token_missing_email_field(self) -> None:
        """Test that email is required"""
        payload = {
            "email": "",
            "password": "password1234",
            "name": "Test API User"
        }
        res = self.client.post(TOKEN_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn("token", res.data)

    def test_create_token_missing_password_field(self) -> None:
        """Test that password is required"""
        payload = {
            "email": "test@gawlowski.com.pl",
            "password": "",
            "name": "Test API User"
        }
        res = self.client.post(TOKEN_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn("token", res.data)
