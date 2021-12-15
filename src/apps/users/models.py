from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)


class UserManager(BaseUserManager):
    """Class to add UserManager to User model"""

    def create_user(self, email: str, password: str = None, **extra_fields):
        """
        Method to create user with email and password
        :param email: string email
        :param password: string password
        :param extra_fields: dict with other fields
        :return: user object QuerySet
        """

        if not email:
            raise ValueError("User must have an email")

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email: str, password: str, **extra_fields):
        """
        Method to create a superuser for admin web siteTrue
        :param email: string email
        :param password: string password
        :return: user object QuerySet
        """

        user = self.create_user(
            email=email, password=password, **extra_fields
        )
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User model"""

    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("username", )
