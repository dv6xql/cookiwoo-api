from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email="test@gawlowski.com.pl", password="password1234"):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self) -> None:
        """Test creating a new user with an email is successful"""
        email = "test@gawlowski.com.pl"
        password = "passworD1234"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self) -> None:
        """Test the email for a new user is normalized"""
        email = "test@GAWLOWSKI.COM.PL"
        user = get_user_model().objects.create_user(
            email=email,
            password="password1234"
        )
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self) -> None:
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=None,
                password='password1234'
            )

    def test_new_user_invalid_password(self) -> None:
        """Test creating user with no password raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email="test@gawlowski.com.pl",
                password=None
            )

    def test_new_user_invalid_password_length(self) -> None:
        """
        Test creating user with a password shorter than 12 chars raises error
        """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email="test@gawlowski.com.pl",
                password="123456789"
            )

    def test_create_new_superuser(self) -> None:
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            email="test@gawlowski.com.pl",
            password="password1234"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self) -> None:
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name="Vegan"
        )

        self.assertEqual(str(tag), tag.name)
