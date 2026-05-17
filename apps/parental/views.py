from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
)

from core.permissions.roles import (
    IsParentUser
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
        IsParentUser,
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
        IsParentUser,
    )


    def get_queryset(
        self
    ):

        return ChildProfile.objects.filter(
            parent=self.request.user
        )