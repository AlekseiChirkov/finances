from django.test import TestCase
from django.contrib.auth import get_user_model


class UserTests(TestCase):
    """Test users models"""

    def test_create_user_with_email_successful(self) -> None:
        """
        Test creating a new user successful with email
        :return: None
        """

        email = 'test@mail.ru'
        password = 'Admin123'
        user = get_user_model().objects.create_user(email, password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_user_email_normalized(self) -> None:
        """
        Test that email for a new user is normalized
        :return: None
        """

        email = 'test@MAIL.COM'
        user = get_user_model().objects.create_user(email, 'Admin123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self) -> None:
        """
        Test creating user with no email raises error
        :return: None
        """

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'Admin123')

    def test_create_new_superuser(self):
        """
        Test creating a new superuser
        :return: None
        """

        user = get_user_model().objects.create_superuser(
            'admin@mail.ru', 'Admin123'
        )

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
