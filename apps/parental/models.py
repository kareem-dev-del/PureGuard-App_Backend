import uuid

from django.db import models

from django.conf import settings


class ChildProfile(
    models.Model
):

    AGE_GROUPS = (

        ("under_10", "Under 10"),

        ("10_15", "10 to 15"),

        ("15_18", "15 to 18"),

    )


    parent = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="children"
    )


    name = models.CharField(
        max_length=100
    )


    age_group = models.CharField(
        max_length=20,
        choices=AGE_GROUPS
    )


    pair_code = models.CharField(
        max_length=12,
        unique=True,
        blank=True
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def save(
        self,
        *args,
        **kwargs
    ):

        if not self.pair_code:

            self.pair_code = str(
                uuid.uuid4()
            )[:8]


        super().save(
            *args,
            **kwargs
        )


    def __str__(self):

        return self.name