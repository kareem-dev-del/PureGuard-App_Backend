from django.contrib import admin
from django.urls import path, include


urlpatterns = [

    path(
        'admin/',
        admin.site.urls
    ),

    path(
        "api/v1/auth/",
        include("apps.identity.urls")
    ),

    path(
    "api/v1/devices/",
    include("apps.device_control.urls")
   ),

]