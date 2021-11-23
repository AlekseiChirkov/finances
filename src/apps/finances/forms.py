from django import forms

from apps.finances.models import (
    Operation, OperationCategory, Account, AccountCategory
)


class OperationCreationForm(forms.ModelForm):
    """Form class for operation creation"""

    class Meta:
        model = Operation
        fields = "__all__"


class OperationCategoryCreationForm(forms.ModelForm):
    """From class for operation category creation"""

    class Meta:
        model = OperationCategory
        fields = "__all__"


class AccountCreationForm(forms.ModelForm):
    """Form class for account creation"""

    class Meta:
        model = Account
        fields = "__all__"


class AccountCategoryCreationForm(forms.ModelForm):
    """Form class for account category creation"""

    class Meta:
        model = AccountCategory
        fields = "__all__"
