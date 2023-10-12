from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from lessons.models import Lesson, Pay
from lessons.paginators import LessonPaginator
from lessons.serializers import LessonSerializer, PaySerializer, LessonCreateSerializer
from users.permissions import IsModerators, IsUsers


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsUsers | IsModerators]
    pagination_class = LessonPaginator

class LessonDetailAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsUsers | IsModerators]

class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonCreateSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsUsers, ~IsModerators]

    def perform_create(self, serializer):
        new_obj = serializer.save()
        new_obj.user = self.request.user
        new_obj.save()

class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsUsers | IsModerators]

class LessonDeleteAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsUsers, ~IsModerators]


class PayCreateAPIView(generics.CreateAPIView):
    serializer_class = PaySerializer
    queryset = Pay.objects.all()
    permission_classes = [IsUsers]

class PayListAPIView(generics.ListAPIView):
    serializer_class = PaySerializer
    queryset = Pay.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('payment_method', 'is_paid')
    ordering_fields = ('date_of_payment',)
    permission_classes = [IsUsers]

class PayDeleteAPIView(generics.DestroyAPIView):
    queryset = Pay.objects.all()
    permission_classes = [IsUsers]
