from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = "test@gawlowski.com.pl"
        password = "passworD1234"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = "test@GAWLOWSKI.COM.PL"
        user = get_user_model().objects.create_user(
            email=email,
            password="password1234"
        )
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=None,
                password='password1234'
            )

    def test_new_user_invalid_password(self):
        """Test creating user with no password raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email="test@gawlowski.com.pl",
                password=None
            )

    def test_new_user_invalid_password_length(self):
        """Test creating user with a password shorter than twelve characters raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email="test@gawlowski.com.pl",
                password="123456789"
            )

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            email="test@gawlowski.com.pl",
            password="password1234"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
