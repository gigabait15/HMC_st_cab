from rest_framework import generics
from lessons.models import Lesson
from lessons.serializers import LessonSerializer


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

class LessonDetailAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

class LessonDeleteAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
