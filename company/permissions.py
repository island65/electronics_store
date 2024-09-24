from rest_framework import permissions


class IsCompanyOwner(permissions.BasePermission):
    """Checks if the user is the owner of the company."""
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class IsSupplierOwner(permissions.BasePermission):
    """Checks if the user is the owner of the supplier."""
    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False
