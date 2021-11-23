from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from apps.finances.models import (
    Operation, OperationCategory, Account, AccountCategory
)


class OperationAdminTests(TestCase):
    """Class to test finances models admin site"""

    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@mail.ru', password='Password123', username='Admin'
        )
        self.user = get_user_model().objects.create_user(
            email='user@mail.ru', password='Password123', username='username'
        )
        self.client.force_login(self.admin_user)
        self.category = OperationCategory.objects.create(title='Category')
        self.operation = Operation.objects.create(
            user=self.user, title='Operation', description='Description',
            category=self.category, amount=Decimal(100.00)
        )

    def test_operations_list(self) -> None:
        """
        Test that operations are listed on operations page
        :return: None
        """

        url = reverse('admin:finances_operation_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.operation.id)
        self.assertContains(res, self.operation.title)

    def test_create_operation_page(self) -> None:
        """
        Test that create operation page works
        :return: None
        """

        url = reverse('admin:finances_operation_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_operation_change_page(self) -> None:
        """
        Test that operation edit page works
        :return: None
        """

        url = reverse(
            'admin:finances_operation_change', args=[self.operation.id]
        )
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)


class OperationCategoryAdminTests(TestCase):
    """Class to test operations category admin site"""

    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@mail.ru', password='Password123', username='Admin'
        )
        self.user = get_user_model().objects.create_user(
            email='user@mail.ru', password='Password123', username='username'
        )
        self.client.force_login(self.admin_user)
        self.category = OperationCategory.objects.create(title='Category')
        self.operation = Operation.objects.create(
            user=self.user, title='Operation', description='Description',
            category=self.category, amount=Decimal(100.00)
        )

    def test_operation_categories_list(self) -> None:
        """
        Test that operation categories list page works
        :return: None
        """

        url = reverse('admin:finances_operationcategory_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.category.id)
        self.assertContains(res, self.category.title)

    def test_operation_category_create_page(self) -> None:
        """
        Test that operation category creation page works
        :return: None
        """

        url = reverse('admin:finances_operationcategory_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_operation_category_change_page(self) -> None:
        """
        Test that operation category change page works
        :return: None
        """

        url = reverse(
            'admin:finances_operationcategory_change', args=[self.category.id]
        )
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)


class AccountAdminTests(TestCase):
    """Class to test accounts admin site"""

    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@mail.ru', password='Password123', username='Admin'
        )
        self.user = get_user_model().objects.create_user(
            email='user@mail.ru', password='Password123', username='username'
        )
        self.client.force_login(self.admin_user)
        self.category = AccountCategory.objects.create(title='Category')
        self.account = Account.objects.create(
            user=self.user, title='Title', description='Description',
            category=self.category, amount=Decimal(100.00)
        )

    def test_account_list(self) -> None:
        """
        Test that account list page works
        :return: None
        """

        url = reverse('admin:finances_account_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.account.id)
        self.assertContains(res, self.account.title)

    def test_account_create_page(self) -> None:
        """
        Test that account creation page works
        :return: None
        """

        url = reverse('admin:finances_account_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_account_change_page(self) -> None:
        """
        Test that account change page works
        :return: None
        """

        url = reverse(
            'admin:finances_account_change', args=[self.account.id]
        )
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)


class AccountCategoryAdminTests(TestCase):
    """Class to test account category admin site"""

    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@mail.ru', password='Password123', username='Admin'
        )
        self.user = get_user_model().objects.create_user(
            email='user@mail.ru', password='Password123', username='username'
        )
        self.client.force_login(self.admin_user)
        self.category = AccountCategory.objects.create(title='Category')
        self.account = Account.objects.create(
            user=self.user, title='Title', description='Description',
            category=self.category, amount=Decimal(100.00)
        )

    def test_account_categories_list(self) -> None:
        """
        Test that account categories list page works
        :return: None
        """

        url = reverse('admin:finances_accountcategory_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.category.id)
        self.assertContains(res, self.category.title)

    def test_account_category_create_page(self) -> None:
        """
        Test that account category creation page works
        :return: None
        """

        url = reverse('admin:finances_accountcategory_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_account_category_change_page(self) -> None:
        """
        Test that account category change page works
        :return: None
        """

        url = reverse(
            'admin:finances_accountcategory_change', args=[self.category.id]
        )
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
