from rest_framework.permissions import BasePermission
from .models import User

class IsActive(BasePermission):

    def has_permission(self, request, view):
        return User.objects.get(username=request.POST.get('username')).is_active 