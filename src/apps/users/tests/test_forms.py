from django.contrib.auth import get_user_model
from django.test import TestCase, RequestFactory

from apps.users.forms import UserCreationForm, UserLoginForm


SIGNUP_DATA = {
    'email': 'admin@mail.ru', 'username': 'username',
    'password1': 'Aleksissanchez98', 'password2': 'Aleksissanchez98'
}
LOGIN_DATA = {'email': 'admin@mail.ru', 'password': 'Aleksissanchez98'}


class UserFormTests(TestCase):
    """Class to test user forms"""

    def setUp(self) -> None:
        self.factory = RequestFactory()

    def test_signup_form_fields(self) -> None:
        """
        Test that form fields are valid
        :return: None
        """

        signup_form = UserCreationForm()

        self.assertIn('email', signup_form.fields)
        self.assertIn('username', signup_form.fields)
        self.assertIn('password1', signup_form.fields)
        self.assertIn('password2', signup_form.fields)

    def test_login_form_fields(self) -> None:
        """
        Method to test valid form
        :return: None
        """

        login_form = UserLoginForm()

        self.assertIn('email', login_form.fields)
        self.assertIn('password', login_form.fields)

    def test_user_creation_form_is_invalid(self) -> None:
        """
        Test that user creation form invalid password similar to email
        :return: None
        """

        form = UserCreationForm()

        self.assertFalse(form.is_valid())

    def test_user_creation_form_is_valid(self) -> None:
        """
        Test that form is valid
        :return: None
        """

        email = LOGIN_DATA['email']
        password = LOGIN_DATA['password']
        data = {'email': email, 'password': password}
        form = UserLoginForm(data)

        self.assertTrue(form.is_valid())

    def test_signup_user_form_saved_successful(self) -> None:
        """
        Test that form saves successfully
        :return: None
        """

        form = UserCreationForm(SIGNUP_DATA)
        form.save()

        user = get_user_model().objects.get(email=SIGNUP_DATA['email'])

        self.assertEqual(user, form.instance)

    def test_login_form_invalid(self) -> None:
        """
        Test that form data invalid
        :return: None
        """

        form = UserLoginForm({'email': 'ga23gasd', 'password': 'asdasgsa'})

        self.assertFalse(form.is_valid())

    def test_login_form_valid(self) -> None:
        """
        Test that user login form works successful
        :return: None
        """

        form = UserLoginForm(LOGIN_DATA)

        self.assertEqual(form.data, LOGIN_DATA)

    def test_signup_form_validation_error(self) -> None:
        """
        Test that passwords validation failed
        :return: None
        """

        invalid_data = {
            'email': 'admin@mail.ru', 'username': 'username',
            'password1': 'Aleksissanchez98', 'password2': 'Admin123'
        }

        with self.assertRaises(AttributeError):
            form = UserCreationForm(invalid_data)
            form.save()








