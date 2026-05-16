from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class Role(models.TextChoices):
    PARENT = "parent", _("Parent")
    CHILD = "child", _("Child")
    RECOVERY = "recovery", _("Recovery")
    ADMIN = "admin", _("Admin")


class User(AbstractUser):

    username = None  # remove username

    email = models.EmailField(unique=True)

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.PARENT
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email