from django.db import models
from django.conf import settings


class Operation(models.Model):
    """Model for operation table"""

    TYPES = (
        ('Income', 'Income'),
        ('Outcome', 'Outcome'),
        ('Transfer', 'Transfer'),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='operation'
    )
    title = models.CharField(
        max_length=128, blank=True
    )
    description = models.TextField()
    type = models.CharField(
        max_length=64, blank=True, choices=TYPES, default='Outcome'
    )
    categories = models.ManyToManyField(
        'OperationCategory', blank=True,
        related_name='operations'
    )
    account_from = models.ForeignKey(
        'Account', on_delete=models.SET_NULL, null=True,
        related_name='operation'
    )
    account_to = models.ForeignKey(
        'Account', on_delete=models.SET_NULL, blank=True, null=True,
        related_name='receive_operation'
    )
    amount = models.DecimalField(
        max_digits=10, decimal_places=2
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title


class OperationCategory(models.Model):
    """Model for operation category table"""

    title = models.CharField(
        max_length=128, blank=True
    )
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, blank=True, null=True,
        related_name='operation_category'
    )

    def __str__(self):
        return self.title


class Account(models.Model):
    """Model for account table"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='account'
    )
    title = models.CharField(
        max_length=128
    )
    description = models.TextField(
        blank=True
    )
    category = models.OneToOneField(
        'AccountCategory', on_delete=models.SET_NULL, null=True, blank=True,
        related_name='account'
    )
    amount = models.DecimalField(
        max_digits=10, decimal_places=2
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title


class AccountCategory(models.Model):
    """Model for account category table"""

    title = models.CharField(
        max_length=128
    )
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, blank=True, null=True,
        related_name='account_category'
    )

    def __str__(self):
        return self.title
