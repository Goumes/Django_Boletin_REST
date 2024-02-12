from rest_framework import permissions
from rest_framework.permissions import BasePermission


class PatinetePermission(BasePermission):
    message = "No puede pazá makina."

    def has_permission(self, request, view):
        if request.user.groups.filter(name="Administradores").exists():
            return True
        else:
            return False

    def has_group(user, group):
        return user.groups.filter(name=group).exists()
