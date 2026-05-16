from django.db import models

from apps.device_control.models import Device


class TelemetryEvent(
    models.Model
):

    EVENT_TYPES = (

        ("blocked_attempt", "Blocked Attempt"),

        ("app_opened", "App Opened"),

        ("screen_time_updated", "Screen Time Updated"),

        ("vpn_started", "VPN Started"),

        ("vpn_stopped", "VPN Stopped"),

        ("rule_triggered", "Rule Triggered"),

        ("focus_session_started", "Focus Session Started"),

        ("relapse_detected", "Relapse Detected"),

    )


    device = models.ForeignKey(
        Device,
        on_delete=models.CASCADE,
        related_name="events"
    )


    event_type = models.CharField(
        max_length=50,
        choices=EVENT_TYPES
    )


    payload = models.JSONField(
        default=dict
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):

        return self.event_type