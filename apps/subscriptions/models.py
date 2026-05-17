from django.db import models
from django.conf import settings


class Subscription(
    models.Model
):

    PLAN_TYPES = (

        ("free", "Free"),

        ("trial", "Trial"),

        ("premium", "Premium"),

    )


    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="subscription"
    )


    plan = models.CharField(
        max_length=20,
        choices=PLAN_TYPES,
        default="free"
    )


    is_active = models.BooleanField(
        default=True
    )


    started_at = models.DateTimeField(
        auto_now_add=True
    )


    expires_at = models.DateTimeField(
        null=True,
        blank=True
    )


    updated_at = models.DateTimeField(
        auto_now=True
    )


    def __str__(self):

        return f"{self.user.email} - {self.plan}"