from rest_framework import serializers
from course.models import Course
from lessons.models import Lesson
from lessons.serializers import LessonSerializer


class CourseSerializer(serializers.ModelSerializer):
    count_lessons = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True)

    class Meta:
        model = Course
        fields = ('name', 'image', 'description', 'lessons', 'count_lessons')

    def get_count_lessons(self, instance):
        return Lesson.objects.filter(choice_course=instance).count()



