from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ModelViewSet
from course.models import Course, Pay
from course.serializers import CourseSerializer, PaySerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class PayListAPIView(generics.ListAPIView):
    serializer_class = PaySerializer
    queryset = Pay.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('payment_method',)
    ordering_fields = ('date_of_payment',)

    def get_queryset(self):
        course_id = self.request.query_params.get('course_id')
        lesson_id = self.request.query_params.get('lesson_id')

        queryset = super().get_queryset()

        if course_id:
            queryset = queryset.filter(paid_course=course_id)
        if lesson_id:
            queryset = queryset.filter(paid_lesson=lesson_id)

        return queryset