from rest_framework import serializers
from .models import DeviceCommand


class DeviceCommandSerializer(serializers.ModelSerializer):

    class Meta:
        model = DeviceCommand
        fields = "__all__"
        read_only_fields = (
            "status",
            "created_at",
            "executed_at",
        )