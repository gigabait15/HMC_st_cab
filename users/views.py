from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from course.models import Pay
from users.models import User
from users.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

