from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from course.models import Course
from course.serializers import CourseSerializer
from users.permissions import IsModerators, IsUsers


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def perform_create(self, serializer):
        new_obj = serializer.save()
        new_obj.user = self.request.user
        new_obj.save()

    def get_permissions(self):
        if self.action in ["create", "delete"]:
            permission_classes = [~IsModerators]
        else:
            permission_classes = [IsModerators | IsUsers]
        return [permission() for permission in permission_classes]

