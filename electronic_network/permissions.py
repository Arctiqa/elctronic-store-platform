from rest_framework import permissions


class IsActiveUser(permissions.BasePermission):
    """Проверка, является ли пользователь активным сотрудником."""

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return request.user.is_active
