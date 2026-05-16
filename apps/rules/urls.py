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
        RuleCreateView.as_view(),
        name="rule-create"
    ),

    # عرض Rules الخاصة بجهاز
    path(
        "device/<int:device_id>/",
        RuleListView.as_view(),
        name="device-rules"
    ),

    # عرض / تعديل / حذف Rule
    path(
        "<int:pk>/",
        RuleDetailView.as_view(),
        name="rule-detail"
    ),

]