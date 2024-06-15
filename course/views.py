from requests import Response
from rest_framework import generics
from rest_framework.decorators import action
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
        serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.action in ["create", "delete"]:
            permission_classes = [~IsModerators]
        else:
            permission_classes = [IsUsers]
        return [permission() for permission in permission_classes]

class SubscriptionViewSet(ModelViewSet):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    permission_classes = [IsUsers, ~IsModerators]

    @action(detail=False, methods=['post'])
    def create_subscription(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

