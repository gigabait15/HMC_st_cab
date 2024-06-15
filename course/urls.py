from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, SubscriptionViewSet


router = DefaultRouter()
router.register(r'', CourseViewSet, basename='course')
router.register(r'subscription', SubscriptionViewSet, basename='subscription')

urlpatterns = [
    path('', include(router.urls)),
]