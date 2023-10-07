from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from course.models import Course
from course.serializers import CourseSerializer
from users.permissions import IsModerators, IsUsers


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsModerators, IsUsers]

