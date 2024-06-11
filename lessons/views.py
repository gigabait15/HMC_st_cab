from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework import generics
from lessons.serializers import *
from users.permissions import IsModerators, IsUsers


class LessonListAPIView(generics.ListAPIView):
    """отвечает за отображение списка сущностей"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('id', 'name', 'description')
    ordering_fields = ('id',)
    permission_classes = [IsUsers, IsModerators]


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """отвечает за отображение одной сущности"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsUsers, IsModerators]


class LessonCreateAPIView(generics.CreateAPIView):
    """отвечает за создание сущности"""
    serializer_class = LessonSerializer
    permission_classes = [IsUsers, ~IsModerators]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LessonUpdateAPIView(generics.UpdateAPIView):
    """отвечает за редактирование сущности"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsUsers, IsModerators]


class LessonDestroyAPIView(generics.DestroyAPIView):
    """отвечает за удаление сущности"""
    queryset = Lesson.objects.all()
    permission_classes = [IsUsers, ~IsModerators]



