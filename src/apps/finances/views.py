from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)

from apps.finances.models import (
    Operation, OperationCategory, Account, AccountCategory
)
from apps.finances.forms import (
    OperationForm, OperationCategoryForm,
    AccountForm, AccountCategoryForm
)


class AccountListView(ListView):
    """View for getting accounts list"""

    model = Account
    queryset = Account.objects.all()
    template_name = 'pages/finances/accounts/account_list.html'

    def get_queryset(self):
        """
        Get user's accounts list
        :return: Account queryset
        """

        user_accounts = self.queryset.filter(user_id=self.request.user.id)
        return user_accounts


class AccountCreateView(CreateView):
    """View for creating account"""

    model = Account
    form_class = AccountForm
    success_url = reverse_lazy('finances:account-list')
    template_name = 'pages/finances/accounts/account_create.html'

    def form_valid(self, form):
        """Auto assign current user to account"""

        operation = form.save(commit=False)
        operation.user = self.request.user
        operation.save()

        return super(AccountCreateView, self).form_valid(form)


class AccountUpdateView(UpdateView):
    """View for updating account"""

    model = Account
    form_class = AccountForm
    success_url = reverse_lazy('finances:account-list')
    template_name = 'pages/finances/accounts/account_update.html'


class AccountDeleteView(DeleteView):
    """View for deleting account"""

    model = Account
    success_url = reverse_lazy('finances:account-list')


class AccountCategoryListView(ListView):
    """View for getting account categories list"""
    model = AccountCategory
    queryset = AccountCategory.objects.all()
    template_name = 'pages/finances/categories/account_category_list.html'


class AccountCategoryCreateView(CreateView):
    """View for creating account category"""

    model = AccountCategory
    form_class = AccountCategoryForm
    success_url = reverse_lazy('finances:account-category-list')
    template_name = 'pages/finances/categories/account_category_create.html'


class AccountCategoryUpdateView(UpdateView):
    """View for updating Account category"""

    model = AccountCategory
    form_class = AccountCategoryForm
    success_url = reverse_lazy('finances:account-category-list')
    template_name = 'pages/finances/categories/account_category_update.html'


class AccountCategoryDeleteView(DeleteView):
    """View for deletion Account category"""

    model = AccountCategory
    success_url = reverse_lazy('finances:account-category-list')


class OperationListView(ListView):
    """View to get list operations"""

    model = Operation
    queryset = Operation.objects.all()
    template_name = 'pages/finances/operations/operation_list.html'

    def get_queryset(self):
        """
        Get user's operations list
        :return: Operation queryset
        """

        user_operations = self.queryset.filter(user_id=self.request.user.id)
        return user_operations


class OperationDetailView(DetailView):
    """View for retrieve operation detail page"""

    model = Operation
    template_name = 'pages/finances/operations/operation_detail.html'


class OperationCreateView(CreateView):
    """View to create operations page"""

    model = Operation
    form_class = OperationForm
    success_url = reverse_lazy('finances:operation-list')
    template_name = 'pages/finances/operations/operation_create.html'

    def form_valid(self, form):
        """Auto assign current user to operation"""

        amount = form.cleaned_data.get('amount')
        operation_type = form.cleaned_data.get('type')
        print(operation_type)
        account = form.cleaned_data.get('account_from')

        account = Account.objects.get(id=account.id)

        if operation_type == 'Outcome':
            account.amount -= amount
            account.save()

        if operation_type == 'Income':
            account.amount += amount
            account.save()

        if operation_type == 'Transfer':
            to_receive_account = form.cleaned_data.get('account_to')
            receive_account = Account.objects.get(id=to_receive_account.id)
            account.amount -= amount
            receive_account.amount += amount
            account.save()
            receive_account.save()

        operation = form.save(commit=False)
        operation.user = self.request.user
        operation.save()

        return super(OperationCreateView, self).form_valid(form)


class OperationUpdateView(UpdateView):
    """View for updating operation"""

    model = Operation
    form_class = OperationForm
    success_url = reverse_lazy('finances:operation-list')
    template_name = 'pages/finances/operations/operation_update.html'


class OperationDeleteView(DeleteView):
    """View for deleting operations"""

    model = Operation
    success_url = reverse_lazy('finances:operation-list')


class OperationCategoryListView(ListView):
    """View for getting operation categories list"""

    model = OperationCategory
    queryset = OperationCategory.objects.all()
    template_name = 'pages/finances/categories/operation_category_list.html'


class OperationCategoryCreateView(CreateView):
    """View for creating operation category"""

    model = OperationCategory
    form_class = OperationCategoryForm
    success_url = reverse_lazy('finances:operation-category-list')
    template_name = 'pages/finances/categories/operation_category_create.html'


class OperationCategoryUpdateView(UpdateView):
    """View for updating operation category"""

    model = OperationCategory
    form_class = OperationCategoryForm
    success_url = reverse_lazy('finances:operation-category-list')
    template_name = 'pages/finances/categories/operation_category_update.html'


class OperationCategoryDeleteView(DeleteView):
    """View for deletion operation category"""

    model = OperationCategory
    success_url = reverse_lazy('finances:operation-category-list')
