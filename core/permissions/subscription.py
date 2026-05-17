from django.utils import timezone

from rest_framework.permissions import BasePermission


class IsPremiumUser(BasePermission):

    def has_permission(self, request, view):

        user = request.user

        # 1) لازم يكون authenticated
        if not user or not user.is_authenticated:
            return False

        # 2) لازم يكون عنده subscription
        if not hasattr(user, "subscription"):
            return False

        subscription = user.subscription

        # 3) لازم يكون active
        if not subscription.is_active:
            return False

        # 4) لو الاشتراك انتهى → رفض
        if (
            subscription.expires_at
            and subscription.expires_at < timezone.now()
        ):
            return False

        # 5) السماح فقط للـ premium (وممكن تضيف trial لو حابب)
        return subscription.plan in ("premium",)