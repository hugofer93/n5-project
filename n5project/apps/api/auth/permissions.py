from rest_framework.permissions import BasePermission

from n5project.apps.core.permissions import Group


class IsOfficerPermission(BasePermission):
    def has_permission(self, request, view):
        is_officer = request.user.groups.filter(
            name=Group.OFFICER_GROUP_NAME).exists()
        return is_officer


class IsPersonPermission(BasePermission):
    def has_permission(self, request, view):
        is_person = request.user.groups.filter(
            name=Group.OFFICER_GROUP_NAME).exists()
        return is_person
