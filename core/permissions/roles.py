from rest_framework.permissions import BasePermission


class HasRole(BasePermission):

    allowed_roles = []

    def has_permission(self, request, view):

        user = request.user

        return (
            user.is_authenticated
            and
            hasattr(user, "role")
            and
            user.role in self.allowed_roles
        )


# =========================
# 👨 Parent
# =========================

class IsParentUser(HasRole):
    allowed_roles = ["parent"]


# =========================
# 🧠 Recovery
# =========================

class IsRecoveryUser(HasRole):
    allowed_roles = ["recovery"]


# =========================
# 🛡️ Admin
# =========================

class IsAdminUser(HasRole):
    allowed_roles = ["admin"]