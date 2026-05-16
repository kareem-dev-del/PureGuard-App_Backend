from django.urls import path

from .views import (
    RecoveryStartView,
    RecoveryMeView,
    RelapseView,
)

urlpatterns = [

    path(
        "start/",
        RecoveryStartView.as_view(),
        name="recovery-start"
    ),

    path(
        "me/",
        RecoveryMeView.as_view(),
        name="recovery-me"
    ),

    path(
        "relapse/",
        RelapseView.as_view(),
        name="recovery-relapse"
    ),

]