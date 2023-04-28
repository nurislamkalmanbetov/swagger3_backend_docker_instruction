from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAuthenticated


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class IsBase(ReadOnly):
    def has_permission(self, request, view):
        return super().has_permission(request, view) or bool(
            request.user and request.user.role == "base"
        )


class IsAdmin(ReadOnly):
    def has_permission(self, request, view):
        return super().has_permission(request, view) or bool(
            request.user and request.user.is_admin
        )


class IsStaff(ReadOnly):
    def has_permission(self, request, view):
        return super().has_permission(request, view) or bool(
            request.user and request.user.is_staff
        )


class IsSuperuser(ReadOnly):
    def has_permission(self, request, view):
        return super().has_permission(request, view) or bool(
            request.user and request.user.is_superuser
        )
