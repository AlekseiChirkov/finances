from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)


from apps.finances.models import (
    Operation, OperationCategory, Account, AccountCategory
)
from apps.finances.forms import (
    OperationCreationForm, OperationCategoryCreationForm,
    AccountCreationForm, AccountCategoryCreationForm
)


class OperationListView(ListView):
    """View to get list operations"""

    model = Operation
    queryset = Operation.objects.all()
    template_name = 'pages/finances/operation_list.html'


class OperationCreateView(CreateView):
    """View to create operations page"""

    model = Operation
    form_class = OperationCreationForm
    success_url = reverse_lazy('operation-list')
    template_name = 'pages/finances/operation_create.html'

    def form_valid(self, form):
        operation = form.save(commit=False)
        operation.user = self.request.user
        operation.save()
        return super(OperationCreateView, self).form_valid(form)


class OperationCategoryListView(ListView):
    model = OperationCategory
    queryset = OperationCategory.objects.all()
    template_name = 'pages/finances/operation_category_list.html'


class OperationCategoryCreateView(CreateView):
    model = OperationCategory
    form_class = OperationCategoryCreationForm
    success_url = reverse_lazy('operation-category-list')
    template_name = 'pages/finances/operation_category_create.html'


class AccountListView(ListView):
    model = Account
    queryset = Account.objects.all()
    template_name = 'pages/finances/account_list.html'


class AccountCreateView(CreateView):
    model = Account
    form_class = AccountCreationForm
    success_url = reverse_lazy('finances:account_list')
    template_name = 'pages/finances/account_create.html'

    def form_valid(self, form):
        operation = form.save(commit=False)
        operation.user = self.request.user
        operation.save()
        return super(AccountCreateView, self).form_valid(form)


class AccountCategoryListView(ListView):
    model = AccountCategory
    queryset = AccountCategory.objects.all()
    template_name = 'pages/finances/account_category_list.html'


class AccountCategoryCreateView(CreateView):
    model = AccountCategory
    form_class = AccountCategoryCreationForm
    success_url = reverse_lazy('finances:account_list')
    template_name = 'pages/finances/account_category_create.html'
