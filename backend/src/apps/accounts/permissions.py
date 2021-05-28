from rest_framework import permissions


class IsProfileOwner(permissions.BasePermission):
    """
    Allows access only to user that has this profile.
    """

    def has_permission(self, request, view):
        return view.user == request.user
