from django.contrib import admin

from apps.finances.models import (
    Operation, OperationCategory, Account, AccountCategory
)


@admin.register(Operation)
class OperationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Operation._meta.fields]

    class Meta:
        model = Operation


@admin.register(OperationCategory)
class OperationCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in OperationCategory._meta.fields]

    class Meta:
        model = OperationCategory


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Account._meta.fields]

    class Meta:
        model = Account


@admin.register(AccountCategory)
class AccountCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in AccountCategory._meta.fields]

    class Meta:
        model = AccountCategory
