from datetime import timedelta

from django.utils import timezone

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import (
    Subscription
)

from .serializers import (
    SubscriptionSerializer
)


class ActivateSubscriptionView(
    APIView
):

    permission_classes = (
        IsAuthenticated,
    )


    def post(
        self,
        request
    ):

        subscription, _ = Subscription.objects.get_or_create(
            user=request.user
        )


        subscription.plan = "premium"

        subscription.is_active = True

        subscription.started_at = timezone.now()

        subscription.expires_at = (
            timezone.now() + timedelta(days=30)
        )

        subscription.save()


        return Response(

            SubscriptionSerializer(
                subscription
            ).data

        )


class MySubscriptionView(
    APIView
):

    permission_classes = (
        IsAuthenticated,
    )


    def get(
        self,
        request
    ):

        subscription, _ = Subscription.objects.get_or_create(
            user=request.user
        )


        # لو الاشتراك انتهى
        if (
            subscription.expires_at
            and subscription.expires_at < timezone.now()
        ):

            subscription.is_active = False

            subscription.plan = "free"

            subscription.save()


        return Response(

            SubscriptionSerializer(
                subscription
            ).data

        )


class CancelSubscriptionView(
    APIView
):

    permission_classes = (
        IsAuthenticated,
    )


    def post(
        self,
        request
    ):

        subscription = request.user.subscription

        subscription.is_active = False

        subscription.plan = "free"

        subscription.save()


        return Response({

            "status": "cancelled"

        })