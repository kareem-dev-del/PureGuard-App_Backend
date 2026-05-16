from django.urls import path

from .views import (
    RuleCreateView,
    RuleListView,
    RuleDetailView,
)

urlpatterns = [

    # إنشاء Rule
    path(
        "",
        RuleCreateView.as_view()
    ),

    # عرض Rules الخاصة بجهاز
    path(
        "device/<int:device_id>/",
        RuleListView.as_view()
    ),

    # عرض / تعديل / حذف Rule
    path(
        "<int:pk>/",
        RuleDetailView.as_view()
    ),

]