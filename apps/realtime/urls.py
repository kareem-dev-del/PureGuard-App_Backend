from django.urls import path
from .views import (
    SendCommandView,
    PendingCommandsView,
    CompleteCommandView
)

urlpatterns = [

    path(
        "send/",
        SendCommandView.as_view()
    ),

    path(
        "pending/",
        PendingCommandsView.as_view()
    ),

    path(
        "<int:pk>/complete/",
        CompleteCommandView.as_view()
    ),

]