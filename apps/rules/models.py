from django.db import models

from apps.device_control.models import Device


class BlockingRule(models.Model):

    RULE_TYPES = (
        ("app", "App"),
        ("website", "Website"),
        ("category", "Category"),
    )

    device = models.ForeignKey(
        Device,
        on_delete=models.CASCADE,
        related_name="rules"
    )

    rule_type = models.CharField(
        max_length=20,
        choices=RULE_TYPES
    )

    target = models.CharField(
        max_length=255
    )

    priority = models.IntegerField(
        default=1
    )

    schedule = models.JSONField(
        null=True,
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        constraints = [

            models.UniqueConstraint(
                fields=[
                    "device",
                    "rule_type",
                    "target",
                ],
                name="unique_rule"
            )

        ]

        ordering = [
            "-priority"
        ]

    def __str__(self):

        return self.target