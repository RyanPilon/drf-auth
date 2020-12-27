from rest_framework import permissions

class IsPurchaserOrReadOnly(permissions.BasePermission):
    def has_object_permissions(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.purchaser.Blog == request.user