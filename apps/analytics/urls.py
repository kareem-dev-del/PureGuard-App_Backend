from django.urls import path

from .views import (
    EventIngestView,
    MyEventsView,
)

urlpatterns = [

    path(
        "ingest/",
        EventIngestView.as_view(),
        name="event-ingest"
    ),

    path(
        "my/",
        MyEventsView.as_view(),
        name="my-events"
    ),

]