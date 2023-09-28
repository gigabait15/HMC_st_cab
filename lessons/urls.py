from django.urls import path
from lessons.views import *


urlpatterns = [
    path('', LessonListAPIView.as_view()),
    path('<int:pk>/', LessonDetailAPIView.as_view()),
    path('create/', LessonCreateAPIView.as_view()),
    path('update/<int:pk>/', LessonUpdateAPIView.as_view()),
    path('delete/<int:pk>/', LessonDeleteAPIView.as_view()),
]