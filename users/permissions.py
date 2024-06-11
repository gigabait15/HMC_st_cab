from rest_framework.permissions import BasePermission


class IsModerators(BasePermission):

    def has_permission(self, request, view):
        """проверка принадлежности пользователя группе"""
        return request.user.groups.filter(name='moderators').exists()

    def has_object_permission(self, request, view, obj):
        if not self.has_permission(request, view):
            return False
        return True


class IsUsers(BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.user.is_superuser