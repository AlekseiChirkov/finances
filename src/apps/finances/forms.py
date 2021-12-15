from django import forms
from django.contrib.auth import get_user_model

from apps.finances.models import (
    Operation, OperationCategory, Account, AccountCategory
)


class OperationCreationForm(forms.ModelForm):
    """Form class for operation creation"""

    user = forms.ModelChoiceField(
        queryset=get_user_model().objects.all(), required=False
    )

    class Meta:
        model = Operation
        fields = (
            'title', 'description', 'category', 'amount'
        )


class OperationCategoryCreationForm(forms.ModelForm):
    """From class for operation category creation"""

    class Meta:
        model = OperationCategory
        fields = "__all__"


class AccountCreationForm(forms.ModelForm):
    """Form class for account creation"""

    user = forms.ModelChoiceField(
        queryset=get_user_model().objects.all(), required=False
    )

    class Meta:
        model = Account
        fields = ('title', 'description', 'category', 'amount')


class AccountCategoryCreationForm(forms.ModelForm):
    """Form class for account category creation"""

    class Meta:
        model = AccountCategory
        fields = "__all__"
