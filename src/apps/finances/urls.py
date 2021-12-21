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
        'operation-detail/<int:pk>',
        views.OperationDetailView.as_view(),
        name='operation-detail'
    ),
    path(
        'operation-create/',
        views.OperationCreateView.as_view(),
        name='operation-create'
    ),
    path(
        'operation-update/<int:pk>',
        views.OperationUpdateView.as_view(),
        name='operation-update'
    ),
    path(
        'operation-delete/<int:pk>',
        views.OperationDeleteView.as_view(),
        name='operation-delete'
    ),
    path(
        'operation-category-list/',
        views.OperationCategoryListView.as_view(),
        name='operation-category-list'
    ),
    path(
        'operation-category-create/',
        views.OperationCategoryCreateView.as_view(),
        name='operation-category-create'
    ),
    path(
        'operation-category-update/<int:pk>',
        views.OperationCategoryUpdateView.as_view(),
        name='operation-category-update'
    ),
    path(
        'operation-category-delete/<int:pk>',
        views.OperationCategoryDeleteView.as_view(),
        name='operation-category-delete'
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
        'account-update/<int:pk>',
        views.AccountUpdateView.as_view(),
        name='account-update'
    ),
    path(
        'account-delete/<int:pk>',
        views.AccountDeleteView.as_view(),
        name='account-delete'
    ),
    path(
        'account-category-list/',
        views.AccountCategoryListView.as_view(),
        name='account-category-list'
    ),
    path(
        'account-category-create/',
        views.AccountCategoryCreateView.as_view(),
        name='account-category-create'
    ),
    path(
        'account-category-update/<int:pk>',
        views.AccountCategoryUpdateView.as_view(),
        name='account-category-update'
    ),
    path(
        'account-category-delete/<int:pk>',
        views.AccountCategoryDeleteView.as_view(),
        name='account-category-delete'
    ),
]

