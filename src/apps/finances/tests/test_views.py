from django.urls import reverse
from django.test import TestCase, RequestFactory
from django.contrib.auth import get_user_model

from apps.finances.models import (
    Operation, OperationCategory, Account, AccountCategory)
from apps.finances.views import (
    OperationListView, OperationCreateView,
    OperationCategoryListView, OperationCategoryCreateView,
    AccountCreateView, AccountCategoryCreateView
)


class OperationViewsTests(TestCase):
    """Class to test operation views"""

    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.user = get_user_model().objects.create_user(
            email='user@mail.ru', username='username', password='Password123'
        )
        self.category = OperationCategory.objects.create(title='Title')


class OperationCategoryViewsTests(TestCase):
    """Class to test operation category views"""

    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.user = get_user_model().objects.create_user(
            email='user@mail.ru', username='username', password='Password123'
        )


class AccountViewsTests(TestCase):
    """Class to test account views"""
    
    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.user = get_user_model().objects.create_user(
            email='user@mail.ru', username='username', password='Password123'
        )
        self.category = AccountCategory.objects.create(title='Title')


class AccountCategoryViewsTests(TestCase):
    """Class to test operation category views"""

    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.user = get_user_model().objects.create_user(
            email='user@mail.ru', username='username', password='Password123'
        )
