from django import forms
from django.contrib.auth import get_user_model

from apps.finances.models import (
    Operation, OperationCategory, Account, AccountCategory
)


class OperationForm(forms.ModelForm):
    """Form class for operation creation"""

    class Meta:
        model = Operation
        fields = (
            'title', 'description', 'type', 'categories',
            'account_from', 'account_to', 'amount'
        )


class OperationCategoryForm(forms.ModelForm):
    """From class for operation category creation"""

    class Meta:
        model = OperationCategory
        fields = "__all__"


class AccountForm(forms.ModelForm):
    """Form class for account creation"""

    class Meta:
        model = Account
        fields = ('title', 'description', 'category', 'amount')


class AccountCategoryForm(forms.ModelForm):
    """Form class for account category creation"""

    class Meta:
        model = AccountCategory
        fields = "__all__"
