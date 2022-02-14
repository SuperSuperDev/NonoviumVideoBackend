from rest_framework import permissions

from .methods import is_nonoviumvideo_editor


class IsMediacmsEditor(permissions.BasePermission):
    def has_permission(self, request, view):
        if is_nonoviumvideo_editor(request.user):
            return True
        return False
