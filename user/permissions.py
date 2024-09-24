from rest_framework import permissions


class IsUsers(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        """Checks if the user is authorized."""
        if obj.email == request.user.email:
            return True
        return False
