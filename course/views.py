from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from course.models import Course, Subscription
from course.paginators import CoursePaginator
from course.serializers import CourseSerializer, SubscriptionSerializer
from users.permissions import IsModerators, IsUsers


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = CoursePaginator

    def perform_create(self, serializer):
        new_obj = serializer.save()
        new_obj.user = self.request.user
        new_obj.save()

    # def get_permissions(self):
    #     if self.action in ["create", "delete"]:
    #         permission_classes = [~IsModerators]
    #     else:
    #         permission_classes = [IsModerators | IsUsers]
    #     return [permission() for permission in permission_classes]

class SubscriptionCreateAPIView(generics.CreateAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    # permission_classes = [IsUsers, ~IsModerators]

class SubscriptionDeleteAPIView(generics.DestroyAPIView):
    queryset = Subscription.objects.all()
    # permission_classes = [IsUsers, ~IsModerators]
