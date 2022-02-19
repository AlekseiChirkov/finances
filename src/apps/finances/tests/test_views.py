from decimal import Decimal

from django.urls import reverse
from django.test import TestCase, RequestFactory
from django.contrib.auth import get_user_model

from apps.finances.forms import AccountForm
from apps.finances.models import (
    Operation, OperationCategory, Account, AccountCategory)
from apps.finances.views import (
    AccountListView, AccountCreateView,
    AccountCategoryListView, AccountCategoryCreateView,
    OperationListView, OperationCreateView,
    OperationCategoryListView, OperationCategoryCreateView,
)


def sample_account_category():
    """
    Function creates sample account category
    """

    return AccountCategory.objects.create(
        title='title'
    )


def sample_account(user: object, title: str, description: str, amount: Decimal):
    """
    Function creates sample account for tests
    """

    return Account.objects.create(
        user=user, title=title, description=description, amount=amount,
        category=sample_account_category(),
    )


class AccountViewTests(TestCase):
    """Tests for account views"""

    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.user = get_user_model()(
            email='Admin@gmail.com', username='Alex', is_active=True,
        )
        self.password = 'Aleksissanchez98'
        self.user.set_password(self.password)
        self.user.save()

    def test_account_list_view(self) -> None:
        """
        Test that account list response is successful
        """

        sample_account(self.user, 'title1', 'desc1', Decimal(100.50))
        sample_account(self.user, 'title2', 'desc2', Decimal(200.10))

        response = self.client.get(reverse("finances:account-list"))
        self.assertEqual(response.status_code, 200)

    def test_account_create_view(self) -> None:
        """
        Test that account creates successful
        """

        account_data = {
            'title': 'Title', 'description': 'Description',
            'category': sample_account_category().id, 'amount': Decimal(100.50)
        }

        request = self.factory.post(reverse("finances:account-create"), data=account_data)
        request.user = self.user

        res = AccountCreateView.as_view()(request)

        self.assertEqual(res.status_code, 302)





