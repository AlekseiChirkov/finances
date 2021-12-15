from django.urls import path

from apps.finances import views


app_name = 'finances'

urlpatterns = [
    path(
        'operation-list/',
        views.OperationListView.as_view(),
        name='operation-list'
    ),
    path(
        'operation-create/',
        views.OperationCreateView.as_view(),
        name='operation-create'
    ),
    path(
        'operation-categories-list/',
        views.OperationCategoryListView.as_view(),
        name='operation-category-list'
    ),
    path(
        'operation-categories-create/',
        views.OperationCategoryCreateView.as_view(),
        name='operation-category-create'
    ),
    path(
        'account-list/',
        views.AccountListView.as_view(),
        name='account-list'
    ),
    path(
        'account-create/',
        views.AccountCreateView.as_view(),
        name='account-create'
    ),
    path(
        'account-categories-list/',
        views.AccountCategoryListView.as_view(),
        name='account-category-list'
    ),
    path(
        'account-categories-create/',
        views.AccountCategoryCreateView.as_view(),
        name='account-category-create'
    ),
]

