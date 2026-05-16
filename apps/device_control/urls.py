from django.urls import path

from .views import (
    DeviceRegisterView,
    MyDevicesView,
)


urlpatterns = [

    path(
        "register/",
        DeviceRegisterView.as_view()
    ),

    path(
        "me/",
        MyDevicesView.as_view()
    ),

]