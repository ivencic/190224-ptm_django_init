from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff


class IsUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated


class IsGuest(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_anonymous
