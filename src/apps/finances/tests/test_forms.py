from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import TestCase, RequestFactory

from apps.finances.models import (
    Operation, OperationCategory, Account, AccountCategory
)
from apps.finances.forms import (
    OperationCreationForm, OperationCategoryCreationForm,
    AccountCreationForm, AccountCategoryCreationForm
)


class OperationCreationFormTests(TestCase):
    """Class to test operation form"""

    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.user = get_user_model().objects.create_user(
            email='admin@mail.ru', username='username', password='Password123'
        )

    def test_operation_creation_form_fields(self) -> None:
        """
        Test that operation creation form fields are valid
        :return: None
        """

        form = OperationCreationForm()

        self.assertIn('user', form.fields)
        self.assertIn('title', form.fields)
        self.assertIn('description', form.fields)
        self.assertIn('category', form.fields)
        self.assertIn('amount', form.fields)

    def test_operation_creation_form_is_invalid(self) -> None:
        """
        Test that operation creation form is invalid
        :return: None
        """

        form = OperationCreationForm({
            'title': 123
        })

        self.assertFalse(form.is_valid())

    def test_operation_creation_form_is_valid(self) -> None:
        """
        Test that operation creation form is valid
        :return: None
        """

        category = OperationCategory.objects.create(title='Title')
        form = OperationCreationForm(
            {
                'title': 'Title', 'description': 'description',
                'category': category, 'amount': Decimal("100.12")
            }
        )
        form.instance.user = self.user,
        form.save()

        operation = Operation.objects.get(user=self.user, title='Title')

        self.assertTrue(form.is_valid())
        self.assertEqual(operation.user, form.instance.user)
        self.assertEqual(operation, form.instance)


class OperationCategoryCreationFormTests(TestCase):
    """Class to test operation category form"""

    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.user = get_user_model().objects.create_user(
            email='admin@mail.ru', username='username', password='Password123'
        )

    def test_operation_category_creation_form_fields(self) -> None:
        """
        Test that operation category creation form fields are valid
        :return: None
        """

        form = OperationCategoryCreationForm()

        self.assertIn('title', form.fields)
        self.assertIn('parent', form.fields)

    def test_operation_category_creation_form_is_invalid(self) -> None:
        """
        Test that operation category creation form is invalid
        :return: None
        """

        form = OperationCategoryCreationForm()

        self.assertFalse(form.is_valid())

    def test_operation_category_creation_form_is_valid(self) -> None:
        """
        Test that operation category creation form is valid
        :return: None
        """

        category = OperationCategory.objects.create(title='Title')
        form = OperationCategoryCreationForm(
            {
                'title': 'Title2', 'parent': category
            }
        )
        form.save()

        category = OperationCategory.objects.get(title='Title2')

        self.assertTrue(form.is_valid())
        self.assertEqual(category, form.instance)


class AccountCreationFormTests(TestCase):
    """Class to test account form"""

    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.user = get_user_model().objects.create_user(
            email='admin@mail.ru', username='username', password='Password123'
        )

    def test_account_creation_form_fields(self) -> None:
        """
        Test that account creation form fields are valid
        :return: None
        """

        form = AccountCreationForm()

        self.assertIn('user', form.fields)
        self.assertIn('title', form.fields)
        self.assertIn('description', form.fields)
        self.assertIn('category', form.fields)
        self.assertIn('amount', form.fields)

    def test_account_creation_form_is_invalid(self) -> None:
        """
        Test that account creation form is invalid
        :return: None
        """

        form = AccountCreationForm({
            'title': 123
        })

        self.assertFalse(form.is_valid())

    def test_account_creation_form_is_valid(self) -> None:
        """
        Test that account creation form is valid
        :return: None
        """

        category = AccountCategory.objects.create(title='Title')
        form = AccountCreationForm(
            {
                'title': 'Title', 'description': 'description',
                'category': category, 'amount': Decimal("100.12")
            }
        )
        form.instance.user = self.user
        form.save()

        account = Account.objects.get(user=self.user, title='Title')

        self.assertTrue(form.is_valid())
        self.assertEqual(account.user, form.instance.user)
        self.assertEqual(account, form.instance)


class AccountCategoryCreationFormTests(TestCase):
    """Class to test account category form"""

    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.user = get_user_model().objects.create_user(
            email='admin@mail.ru', username='username', password='Password123'
        )

    def test_account_category_creation_form_fields(self) -> None:
        """
        Test that account category creation form fields are valid
        :return: None
        """

        form = AccountCategoryCreationForm()

        self.assertIn('title', form.fields)
        self.assertIn('parent', form.fields)

    def test_account_category_creation_form_is_invalid(self) -> None:
        """
        Test that account category creation form is invalid
        :return: None
        """

        form = AccountCategoryCreationForm()

        self.assertFalse(form.is_valid())

    def test_account_category_creation_form_is_valid(self) -> None:
        """
        Test that account category creation form is valid
        :return: None
        """

        category = AccountCategory.objects.create(title='Title')
        form = AccountCategoryCreationForm(
            {
                'title': 'Title2', 'parent': category
            }
        )
        form.save()

        category = AccountCategory.objects.get(title='Title2')

        self.assertTrue(form.is_valid())
        self.assertEqual(category, form.instance)
