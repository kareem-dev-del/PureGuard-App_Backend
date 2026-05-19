from django.db import models
from apps.device_control.models import Device


class DeviceCommand(models.Model):

    class CommandTypes(models.TextChoices):
        LOCK_DEVICE = "lock_device", "Lock Device"
        UNLOCK_DEVICE = "unlock_device", "Unlock Device"
        SYNC_RULES = "sync_rules", "Sync Rules"
        ENABLE_FOCUS = "enable_focus", "Enable Focus"
        DISABLE_FOCUS = "disable_focus", "Disable Focus"
        BLOCK_APP = "block_app", "Block App"


    class StatusTypes(models.TextChoices):
        PENDING = "pending", "Pending"
        COMPLETED = "completed", "Completed"
        FAILED = "failed", "Failed"


    device = models.ForeignKey(
        Device,
        on_delete=models.CASCADE,
        related_name="commands"
    )

    command_type = models.CharField(
        max_length=50,
        choices=CommandTypes.choices
    )

    payload = models.JSONField(default=dict, blank=True)

    status = models.CharField(
        max_length=20,
        choices=StatusTypes.choices,
        default=StatusTypes.PENDING
    )

    created_at = models.DateTimeField(auto_now_add=True)

    executed_at = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return f"{self.device.id} - {self.command_type}"