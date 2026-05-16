from django.urls import path

from .views import (
    ChildCreateView,
    MyChildrenView,
)

urlpatterns = [

    path(
        "",
        ChildCreateView.as_view(),
        name="child-create"
    ),

    path(
        "my/",
        MyChildrenView.as_view(),
        name="my-children"
    ),

]