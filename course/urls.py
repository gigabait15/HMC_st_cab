from django.urls import path
from rest_framework.routers import DefaultRouter
from course.views import CourseViewSet, SubscriptionDeleteAPIView, SubscriptionCreateAPIView

router = DefaultRouter()
router.register(r'', CourseViewSet, basename='course')

urlpatterns = [
    path('subscription/create/', SubscriptionCreateAPIView.as_view()),
    path('subscription/delete/<int:pk>/', SubscriptionDeleteAPIView.as_view()),
] + router.urls