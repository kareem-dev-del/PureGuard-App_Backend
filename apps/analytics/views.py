from rest_framework.permissions import (
    IsAuthenticated
)

from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
)

from rest_framework.exceptions import (
    PermissionDenied
)

from .models import (
    TelemetryEvent
)

from .serializers import (
    TelemetryEventSerializer
)


class EventIngestView(
    CreateAPIView
):

    serializer_class = (
        TelemetryEventSerializer
    )

    permission_classes = (
        IsAuthenticated,
    )


    def perform_create(
        self,
        serializer
    ):

        device = serializer.validated_data[
            "device"
        ]


        if device.user != self.request.user:

            raise PermissionDenied(
                "Invalid device."
            )


        serializer.save()


class MyEventsView(
    ListAPIView
):

    serializer_class = (
        TelemetryEventSerializer
    )

    permission_classes = (
        IsAuthenticated,
    )


    def get_queryset(
        self
    ):

        return TelemetryEvent.objects.filter(
            device__user=self.request.user
        ).order_by(
            "-created_at"
        )