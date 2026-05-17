from django.urls import path
from .views import PairDeviceView

urlpatterns = [

    path(
        "verify/",
        PairDeviceView.as_view()
    ),

]