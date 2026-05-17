from django.db import models
from django.conf import settings


class Device(models.Model):

    PLATFORM_CHOICES = (
        ("android", "Android"),
        ("ios", "iOS"),
    )

    child = models.ForeignKey(
    "parental.ChildProfile",
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name="devices"
   )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="devices"
    )

    device_uuid = models.CharField(
        max_length=255,
        unique=True
    )

    platform = models.CharField(
        max_length=20,
        choices=PLATFORM_CHOICES
    )

    is_active = models.BooleanField(
        default=True
    )

    rules_version = models.IntegerField(
        default=1
    )

    last_seen = models.DateTimeField(
        auto_now=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return self.device_uuid