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

   path(
    "api/v1/rules/",
    include("apps.rules.urls")
   ),

   path(
    "api/v1/events/",
    include("apps.analytics.urls")
   ),

   path(
    "api/v1/children/",
    include("apps.parental.urls")
    ),

    path(
    "api/v1/reports/",
    include("apps.reports.urls")
   ),

   path(
    "api/v1/recovery/",
    include("apps.recovery.urls")
    ),

]