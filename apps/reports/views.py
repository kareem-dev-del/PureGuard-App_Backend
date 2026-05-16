from django.db.models import Count

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.analytics.models import (
    TelemetryEvent
)


class DashboardView(
    APIView
):

    permission_classes = (
        IsAuthenticated,
    )


    def get(
        self,
        request
    ):

        events = TelemetryEvent.objects.filter(
            device__user=request.user
        )


        total_events = events.count()


        blocked_attempts = events.filter(
            event_type="blocked_attempt"
        ).count()


        relapse_count = events.filter(
            event_type="relapse_detected"
        ).count()


        top_events = list(

            events.values(
                "event_type"
            ).annotate(

                total=Count(
                    "id"
                )

            ).order_by(
                "-total"
            )[:5]

        )


        return Response({

            "total_events":
                total_events,

            "blocked_attempts":
                blocked_attempts,

            "relapse_count":
                relapse_count,

            "top_events":
                top_events,

        })