from django.utils import timezone

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import (
    RecoveryProfile
)

from .serializers import (
    RecoverySerializer
)


class RecoveryStartView(
    APIView
):

    permission_classes = (
        IsAuthenticated,
    )


    def post(
        self,
        request
    ):

        profile, _ = RecoveryProfile.objects.get_or_create(
            user=request.user
        )


        return Response(

            RecoverySerializer(
                profile
            ).data

        )


class RecoveryMeView(
    APIView
):

    permission_classes = (
        IsAuthenticated,
    )


    def get(
        self,
        request
    ):

        profile = request.user.recovery_profile


        return Response(

            RecoverySerializer(
                profile
            ).data

        )


class RelapseView(
    APIView
):

    permission_classes = (
        IsAuthenticated,
    )


    def post(
        self,
        request
    ):

        profile = request.user.recovery_profile


        profile.relapse_count += 1

        profile.current_streak = 0

        profile.last_relapse_at = timezone.now()


        profile.save()


        return Response(

            RecoverySerializer(
                profile
            ).data

        )