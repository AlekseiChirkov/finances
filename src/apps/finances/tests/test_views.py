from decimal import Decimal

from django.urls import reverse
from django.test import TestCase, RequestFactory
from django.contrib.auth import get_user_model

from apps.finances.models import OperationCategory, AccountCategory
from apps.users.views import (
    OperationCreateView, OperationCategoryCreateView, AccountCreateView,
    AccountCategoryCreateView
)


class OperationViewsTests(TestCase):
    """Class to test operation views"""

    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.user = get_user_model().objects.create_user(
            email='user@mail.ru', username='username', password='Password123'
        )
        self.category = OperationCategory.objects.create(title='Title')

    def test_operation_create_page_status_code_is_ok(self) -> None:
        """
        Test that operation create page status code 200
        :return: None
        """

        request = self.factory.get(reverse('finances:operation-create'))
        res = OperationCreateView.as_view()(request)

        self.assertEqual(res.status_code, 200)

    def test_operation_creation_status_code(self) -> None:
        """
        Test that operation creates successfully and status code is 302
        :return: None
        """

        request = self.factory.post(
            reverse('finances:operation-create'), data={
                'user': self.user, 'title': 'Title', 'description': 'Desc',
                'category': self.category, 'amount': Decimal('100.23')
            }
        )
        res = OperationCreateView.as_view()(request)

        self.assertEqual(res.status_code, 302)

    def test_operation_create_invalid_request(self) -> None:
        """
        Test that operation create request is invalid
        :return: None
        """

        request = self.factory.post(reverse('finances:operation-create'))
        res = OperationCreateView.as_view()(request)

        self.assertEqual(res.status_code, 200)


class OperationCategoryViewsTests(TestCase):
    """Class to test operation category views"""

    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.user = get_user_model().objects.create_user(
            email='user@mail.ru', username='username', password='Password123'
        )

    def test_operation_category_create_page_status_code_is_ok(self) -> None:
        """
        Test that operation category page status code is 200
        :return: None
        """

        request = self.factory.get(
            reverse('finances:operation-category-create')
        )
        res = OperationCategoryCreateView.as_view()(request)

        self.assertEqual(res.status_code, 200)

    def test_operation_category_creation_status_code(self) -> None:
        """
        Test that operation category creation request status code is 302
        :return: None
        """

        request = self.factory.post(
            reverse('finances:operation-category-create'),
            data={'title': 'Title'}
        )
        res = OperationCategoryCreateView.as_view()(request)

        self.assertEqual(res.status_code, 302)

    def test_operation_creation_invalid_request(self) -> None:
        """
        Test that operation category creation request is invalid
        :return: None
        """

        request = self.factory.post(
            reverse('finances:operation-category-create')
        )
        res = OperationCategoryCreateView.as_view()(request)

        self.assertEqual(res.status_code, 200)


class AccountViewsTests(TestCase):
    """Class to test account views"""
    
    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.user = get_user_model().objects.create_user(
            email='user@mail.ru', username='username', password='Password123'
        )
        self.category = AccountCategory.objects.create(title='Title')
    
    def test_account_create_page_status_code_is_ok(self) -> None:
        """
        Test that account create pages status code 200
        :return: None
        """

        request = self.factory.get(reverse('finances:account-create'))
        res = AccountCreateView.as_view()(request)

        self.assertEqual(res.status_code, 200)

    def test_account_creation_status_code(self) -> None:
        """
        Test that account creates successfully and status code is 302
        :return: None
        """

        request = self.factory.post(
            reverse('finances:account-create'),
            data={
                'user': self.user, 'title': 'Title', 'description': 'Desc',
                'category': self.category, 'amount': Decimal('100.23')
            }
        )
        res = OperationCreateView.as_view()(request)

        self.assertEqual(res.status_code, 302)

    def test_operation_create_invalid_request(self) -> None:
        """
        Test that operation create request is invalid
        :return: None
        """

        request = self.factory.post('finances:account-create')
        res = OperationCreateView.as_view()(request)

        self.assertEqual(res.status_code, 200)


class AccountCategoryViewsTests(TestCase):
    """Class to test operation category views"""

    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.user = get_user_model().objects.create_user(
            email='user@mail.ru', username='username', password='Password123'
        )

    def test_account_category_create_page_status_code_is_ok(self) -> None:
        """
        Test that operation category page status code is 200
        :return: None
        """

        request = self.factory.get(reverse('finances:account-category-create'))
        res = AccountCategoryCreateView.as_view()(request)

        self.assertEqual(res.status_code, 200)

    def test_account_category_creation_status_code(self) -> None:
        """
        Test that operation category creation request status code 302
        :return: None
        """

        request = self.factory.post(
            reverse('finances:account-category-create'),
            data={'title': 'Title'}
        )
        res = AccountCategoryCreateView.as_view()(request)

        self.assertEqual(res.status_code, 302)

    def test_account_category_creation_invalid_request(self) -> None:
        """
        Test that account category creation request is invalid
        :return: None
        """

        request = self.factory.post(
            reverse('finances:account-category-create')
        )
        res = AccountCategoryCreateView.as_view()(request)

        self.assertEqual(res.status_code, 200)
