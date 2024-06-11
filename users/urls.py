from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import *
from users.apps import UsersConfig


app_name = UsersConfig.name

router = DefaultRouter()
router.register(r'pay', PayViewSet, basename='pay')

urlpatterns = [
        path('list/', UserListAPIView.as_view(), name='User_list'),
        path('detail/<int:pk>/', UserRetrieveAPIView.as_view(), name='User_detail'),
        path('create/', UserCreateAPIView.as_view(), name='User_create'),
        path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='User_update'),
        path('delete/<int:pk>/', UserDestroyAPIView.as_view(), name='User_delete'),

        path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
        ] + router.urls
