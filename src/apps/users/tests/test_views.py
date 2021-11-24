from django.urls import reverse
from django.test import TestCase, RequestFactory
from django.contrib.auth import get_user_model

from apps.users.views import UserSignUpFormView, UserLoginFormView


SIGNUP_DATA = {
    'email': 'admin@mail.ru', 'username': 'username',
    'password1': 'Aleksissanchez98', 'password2': 'Aleksissanchez98'
}
LOGIN_DATA = {
    'email': 'Admin@gmail.com', 'username': 'Alex',
    'password': 'Aleksissanchez98'
}


class UserViewsTests(TestCase):
    """Test user views"""

    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.user = get_user_model()(
            email='Admin@gmail.com', username='Alex', is_active=True,
        )
        self.password = 'Aleksissanchez98'
        self.user.set_password(self.password)
        self.user.save()

    def test_signup_page_status_code(self) -> None:
        """
        Method to test signup page status code 200
        :return: None
        """

        request = self.factory.get(reverse('users:signup'))
        res = UserSignUpFormView.as_view()(request)

        self.assertEqual(res.status_code, 200)

    def test_login_page_status_code(self) -> None:
        """
        Test that login page status code 200
        :return: None
        """

        request = self.factory.get(reverse('users:login'))
        res = UserLoginFormView.as_view()(request)

        self.assertEqual(res.status_code, 200)

    def test_user_signup_creation_status_code(self) -> None:
        """
        Test that user creates successfully and status code is 302
        :return: None
        """

        request = self.factory.post(reverse('users:signup'), data=SIGNUP_DATA)
        request.user = self.user

        res = UserSignUpFormView.as_view()(request)

        self.assertEqual(res.status_code, 302)

    def test_form_invalid_view(self) -> None:
        """
        Test that form view is invalid
        :return: None
        """

        request = self.factory.post(reverse('users:signup'))
        res = UserSignUpFormView.as_view()(request)

        self.assertEqual(res.status_code, 200)

    def test_user_login_form_valid(self) -> None:
        """
        Test that user login form is valid
        :return: None
        """

        res = self.client.post(reverse('users:login'), LOGIN_DATA)

        self.assertEqual(res.status_code, 302)

    def test_user_login_form_invalid(self) -> None:
        """
        Test that user login form is invalid
        :return: None
        """

        request = self.factory.post(reverse('users:signup'))
        res = UserLoginFormView.as_view()(request)

        self.assertEqual(res.status_code, 200)
