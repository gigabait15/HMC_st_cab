from requests import Response
from rest_framework import generics, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework import permissions

from users.models import *
from users.permissions import IsUsers
from users.serializers import *


class PayViewSet(viewsets.ModelViewSet):
    serializer_class = PaySerializer
    queryset = Pay.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course', 'user', 'payment_method')
    ordering_fields = ('date_of_payment',)


class UserListAPIView(generics.ListAPIView):
    """отвечает за отображение списка сущностей"""
    serializer_class = PrivateUserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """отвечает за отображение одной сущности"""
    serializer_class = PublicUserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if getattr(self, 'swagger_fake_view', False):
            return PublicUserSerializer
        if self.request.user != self.get_object():
            return PublicUserSerializer
        return PrivateUserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """отвечает за создание сущности"""
    serializer_class = PrivateUserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(generics.UpdateAPIView):
    """отвечает за редактирование сущности"""
    serializer_class = PrivateUserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsUsers]


class UserDestroyAPIView(generics.DestroyAPIView):
    """отвечает за удаление сущности"""
    serializer_class = PrivateUserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsUsers]
