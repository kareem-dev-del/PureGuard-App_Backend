from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
)

from rest_framework.permissions import IsAuthenticated

from .models import Device
from .serializers import DeviceSerializer


class DeviceRegisterView(CreateAPIView):

    serializer_class = DeviceSerializer

    permission_classes = (
        IsAuthenticated,
    )


    def perform_create(self, serializer):

        serializer.save(
            user=self.request.user
        )


class MyDevicesView(ListAPIView):

    serializer_class = DeviceSerializer

    permission_classes = (
        IsAuthenticated,
    )


    def get_queryset(self):

        return Device.objects.filter(
            user=self.request.user
        )