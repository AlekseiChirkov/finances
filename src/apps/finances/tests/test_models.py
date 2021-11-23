from decimal import Decimal

from django.test import TestCase
from django.contrib.auth import get_user_model

from apps.finances.models import (
    Operation, OperationCategory, Account, AccountCategory
)


class ModelTests(TestCase):
    """Class to test models"""
    
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            email='admin@mail.ru', username='Alex', password='Password123'
        )
    
    def test_operation_str(self) -> None:
        """
        Test that operation model string representation is correct
        :return: None
        """

        category = OperationCategory.objects.create(title='Category')
        operation = Operation.objects.create(
            user=self.user, title='Operation', description='Description',
            category=category, amount=Decimal(100.00)
        )

        self.assertEqual(str(operation), operation.title)

    def test_operation_category_str(self) -> None:
        """
        Test that operation category model string representation is correct
        :return: None
        """

        category = OperationCategory.objects.create(title='Category')

        self.assertEqual(str(category), category.title)

    def test_account_str(self) -> None:
        """
        Test that account model string representation is correct
        :return: None
        """

        category = AccountCategory.objects.create(title='Category')
        account = Account.objects.create(
            user=self.user, title='Title', description='Description',
            category=category, amount=Decimal(100.00)
        )

        self.assertEqual(str(account), account.title)

    def test_account_category_str(self) -> None:
        """
        Test that account category model string representation is correct
        :return: None
        """

        category = AccountCategory.objects.create(title='Title')

        self.assertEqual(str(category), category.title)
