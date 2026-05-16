from rest_framework.permissions import (
    IsAuthenticated
)

from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)

from rest_framework.exceptions import (
    PermissionDenied
)

from .models import BlockingRule

from .serializers import (
    BlockingRuleSerializer
)


class RuleCreateView(
    CreateAPIView
):

    serializer_class = (
        BlockingRuleSerializer
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

        # التأكد إن الجهاز تابع للمستخدم الحالي
        if device.user != self.request.user:

            raise PermissionDenied(
                "You cannot add rules to this device."
            )

        serializer.save()


class RuleListView(
    ListAPIView
):

    serializer_class = (
        BlockingRuleSerializer
    )

    permission_classes = (
        IsAuthenticated,
    )

    def get_queryset(self):

        device_id = self.kwargs[
            "device_id"
        ]

        return BlockingRule.objects.filter(
            device_id=device_id,
            device__user=self.request.user
        ).order_by("-priority")


class RuleDetailView(
    RetrieveUpdateDestroyAPIView
):

    serializer_class = (
        BlockingRuleSerializer
    )

    permission_classes = (
        IsAuthenticated,
    )

    def get_queryset(self):

        return BlockingRule.objects.filter(
            device__user=self.request.user
        )