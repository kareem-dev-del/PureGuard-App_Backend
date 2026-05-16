from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


class UserAdmin(BaseUserAdmin):

    model = User

    list_display = (
        "email",
        "role",
        "is_staff",
        "is_active",
        "created_at",
        "updated_at",
    )

    list_filter = ("role", "is_staff", "is_active")

    search_fields = ("email",)
    ordering = ("email",)

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Info", {"fields": ("role",)}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser")}),
        ("Important dates", {"fields": ("last_login", "created_at", "updated_at")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2", "role", "is_staff", "is_active")
        }),
    )


admin.site.register(User, UserAdmin)