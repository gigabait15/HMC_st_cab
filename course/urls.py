from django.urls import path
from rest_framework.routers import DefaultRouter
from course.views import CourseViewSet, PayListAPIView

router = DefaultRouter()
router.register(r'', CourseViewSet, basename='course')

urlpatterns = [
    path('pay/', PayListAPIView.as_view())
] + router.urls