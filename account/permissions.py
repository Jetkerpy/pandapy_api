from rest_framework.permissions import BasePermission


class IsOwnerOfProfile(BasePermission):
    """
        For profile permission, if user is authenticated and 
        owner of profile
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated


    def has_object_permission(self, request, view, obj):
        return request.user.pk == obj.pk