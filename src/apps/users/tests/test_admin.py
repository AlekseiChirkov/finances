from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class UserAdminTests(TestCase):
    """Class to test users admin site"""

    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@mail.ru', password='Password123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='test@mail.ru', username='username', password='Admin123'
        )

    def test_users_list(self) -> None:
        """
        Test that users are listed on users page
        :return: None
        """

        url = reverse('admin:users_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.username)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self) -> None:
        """
        Test that user edit page works
        :return: None
        """

        url = reverse('admin:users_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self) -> None:
        """
        Test that create user page works
        :return: None
        """

        url = reverse('admin:users_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
