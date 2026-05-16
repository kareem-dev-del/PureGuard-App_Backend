from django.db import models

from django.conf import settings


class RecoveryProfile(
    models.Model
):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="recovery_profile"
    )


    current_streak = models.IntegerField(
        default=0
    )


    longest_streak = models.IntegerField(
        default=0
    )


    relapse_count = models.IntegerField(
        default=0
    )


    last_relapse_at = models.DateTimeField(
        null=True,
        blank=True
    )


    started_at = models.DateTimeField(
        auto_now_add=True
    )


    updated_at = models.DateTimeField(
        auto_now=True
    )


    def __str__(self):

        return str(
            self.user.email
        )