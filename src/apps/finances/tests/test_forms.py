from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import TestCase, RequestFactory

from apps.finances.models import (
    Operation, OperationCategory, Account, AccountCategory
)
from apps.finances.forms import (
    OperationCreationForm, OperationCategoryCreationForm,
    AccountCreationForm, AccountCategoryCreationFrom
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
        self.assertIn('created_at', form.fields)

    def test_operation_creation_form_is_invalid(self) -> None:
        """
        Test that operation creation form is invalid
        :return: None
        """

        form = OperationCreationForm({
            'title': 123
        })

        self.assertFalse(form.is_valid)

    def test_operation_creation_form_is_valid(self) -> None:
        """
        Test that operation creation form is valid
        :return: None
        """

        category = OperationCategory.objects.create(title='Title')
        form = OperationCreationForm(
            {
                'user': self.user, 'title': 'Title',
                'description': 'description', 'category': category,
                'amount': Decimal(100.12)
            }
        )
        form.save()

        operation = Operation.objects.get(user=self.user, title='Title')

        self.assertTrue(form.is_valid())
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

        form = OperationCategoryCreationForm({
            'title': 123
        })

        self.assertFalse(form.is_valid)

    def test_operation_creation_form_is_valid(self) -> None:
        """
        Test that operation creation form is valid
        :return: None
        """

        category = OperationCategory.objects.create(title='Title')
        form = OperationCreationForm(
            {
                'title': 'Title2', 'parent': category
            }
        )
        form.save()

        category = OperationCategory.objects.get(title='Title2')

        self.assertTrue(form.is_valid())
        self.assertEqual(category, form.instance)


