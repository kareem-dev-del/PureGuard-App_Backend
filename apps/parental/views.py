from rest_framework.permissions import (
    IsAuthenticated
)

from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
)

from .models import (
    ChildProfile
)

from .serializers import (
    ChildSerializer
)


class ChildCreateView(
    CreateAPIView
):

    serializer_class = (
        ChildSerializer
    )

    permission_classes = (
        IsAuthenticated,
    )


    def perform_create(
        self,
        serializer
    ):

        serializer.save(
            parent=self.request.user
        )


class MyChildrenView(
    ListAPIView
):

    serializer_class = (
        ChildSerializer
    )

    permission_classes = (
        IsAuthenticated,
    )


    def get_queryset(
        self
    ):

        return ChildProfile.objects.filter(
            parent=self.request.user
        )