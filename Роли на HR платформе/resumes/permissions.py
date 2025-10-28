from rest_framework.permissions import BasePermission, SAFE_METHODS


class ResumePermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        if request.user.role == 'admin':
            return True
        if request.user.role == 'hr_manager':
            return request.method in SAFE_METHODS
        if request.user.role == 'candidate':
            return request.method in ['GET', 'POST', 'PUT', 'PATCH']
        return False

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False

        if request.user.role == 'admin':
            return True
        if request.user.role == 'hr_manager':
            return request.method in SAFE_METHODS
        if request.user.role == 'candidate':
            return obj.user == request.user
        return False
