from rest_framework import permissions


class IsAuthor(permissions.BasePermission):
    """
    Allows access only to the user who is the author or one of the authors for this article.
    """

    def has_permission(self, request, view):
        return bool(view.get_object().authors.filter(id=request.user.id))


class IsFilledUser(permissions.BasePermission):
    """
    Allows access only to the user who is the author or one of the authors for this article.
    """

    def has_permission(self, request, view):
        return request.user.is_filled
