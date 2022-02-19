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

