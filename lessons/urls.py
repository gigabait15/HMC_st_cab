from django.urls import path
from lessons.apps import LessonsConfig
from lessons.views import *

app_name = LessonsConfig.name

urlpatterns = [
    path('list/', LessonListAPIView.as_view(), name='lesson_list'),
    path('detail/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_detail'),
    path('create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_delete'),
]