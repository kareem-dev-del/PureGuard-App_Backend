from django.urls import path

from .views import (
    DeviceRegisterView,
    MyDevicesView,
)

urlpatterns = [

    path(
        "register/",
        DeviceRegisterView.as_view(),
        name="device-register"
    ),

    path(
        "me/",
        MyDevicesView.as_view(),
        name="my-devices"
    ),

]