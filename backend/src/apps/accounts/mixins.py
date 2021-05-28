from rest_framework.generics import get_object_or_404

from src.apps.accounts.models import User


class UserViewMixin:
    user_lookup_field = None

    @property
    def user_pk(self):
        return int(self.kwargs[self.user_lookup_field])

    @property
    def user(self):
        if self.user_lookup_field:
            return get_object_or_404(User, pk=self.user_pk)
        return self.get_user()

    def get_user(self):
        return self.get_object()


class PermissionPerActionMixin:
    permission_classes_by_action = None

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [
                permission()
                for permission in self.permission_classes_by_action[self.action]
            ]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]
