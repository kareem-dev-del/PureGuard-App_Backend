from django.urls import path

from .views import (
    ActivateSubscriptionView,
    MySubscriptionView,
    CancelSubscriptionView,
)

urlpatterns = [

    path(
        "activate/",
        ActivateSubscriptionView.as_view(),
        name="subscription-activate"
    ),

    path(
        "me/",
        MySubscriptionView.as_view(),
        name="subscription-me"
    ),

    path(
        "cancel/",
        CancelSubscriptionView.as_view(),
        name="subscription-cancel"
    ),

]