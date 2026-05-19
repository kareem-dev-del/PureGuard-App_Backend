from django.utils import timezone
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from .models import DeviceCommand
from .serializers import DeviceCommandSerializer

from apps.device_control.models import Device


class SendCommandView(APIView):

    permission_classes = (IsAuthenticated,)

    def post(self, request):

        device_id = request.data.get("device_id")
        command_type = request.data.get("command_type")
        payload = request.data.get("payload", {})

        if not device_id or not command_type:
            raise ValidationError("device_id and command_type are required")

        device = get_object_or_404(
            Device,
            id=device_id,
            user=request.user
        )

        command = DeviceCommand.objects.create(
            device=device,
            command_type=command_type,
            payload=payload
        )

        return Response(DeviceCommandSerializer(command).data)
    

class PendingCommandsView(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request):

        device_id = request.query_params.get("device_id")

        if not device_id:
            raise ValidationError("device_id is required")

        device = get_object_or_404(
            Device,
            id=device_id,
            user=request.user
        )

        commands = DeviceCommand.objects.filter(
            device=device,
            status=DeviceCommand.StatusTypes.PENDING
        ).order_by("created_at")

        return Response(
            DeviceCommandSerializer(commands, many=True).data
        )



class CompleteCommandView(APIView):

    permission_classes = (IsAuthenticated,)

    def post(self, request, pk):

        command = get_object_or_404(
            DeviceCommand,
            id=pk
        )

        if command.device.user != request.user:
            raise ValidationError("Not allowed")

        command.status = DeviceCommand.StatusTypes.COMPLETED
        command.executed_at = timezone.now()
        command.save()

        return Response({
            "status": "completed"
        })
    

   