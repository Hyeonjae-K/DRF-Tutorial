from rest_framework import permissions

from .permissions import IsStaffEditorPermission


class StaffEditorPermissionMixin():
    permission_classes = [
        permissions.IsAdminUser,
        IsStaffEditorPermission
    ]


class UserQuerysetMixin():
    user_field = 'user'
    allow_staff_viwe = False

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        lookup_data = {}
        lookup_data[self.user_field] = user
        print(lookup_data)

        qs = super().get_queryset()
        print(qs)

        if self.allow_staff_viwe and user.is_staff:
            return qs

        return qs.filter(**lookup_data)
