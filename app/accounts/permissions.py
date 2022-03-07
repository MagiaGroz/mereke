from rest_framework.permissions import BasePermission, SAFE_METHODS
from .serializers import UserProfileSerializer


class IsOwnerProfileOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if obj.user == request.user:
            return True

        user = UserProfileSerializer(obj.user)
        if user['is_admin'] is True:
            return True

        return False