from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from apps.device_control.models import Device
from apps.parental.models import ChildProfile


class PairDeviceView(APIView):

    permission_classes = (
        IsAuthenticated,
    )


    def post(
        self,
        request
    ):

        device_id = request.data.get(
            "device_id"
        )

        pair_code = request.data.get(
            "pair_code"
        )


        try:

            device = Device.objects.get(
                id=device_id,
                user=request.user
            )

        except Device.DoesNotExist:

            raise ValidationError(
                "Invalid device."
            )


        try:

            child = ChildProfile.objects.get(
                pair_code=pair_code,
                parent=request.user
            )

        except ChildProfile.DoesNotExist:

            raise ValidationError(
                "Invalid pair code."
            )


        device.child = child

        device.rules_version += 1

        device.save()


        return Response({

            "status":
                "paired",

            "child":
                child.name,

        })