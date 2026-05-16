from rest_framework import serializers

from .models import (
    RecoveryProfile
)


class RecoverySerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = RecoveryProfile

        fields = "__all__"

        read_only_fields = (
            "user",
        )