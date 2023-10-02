from rest_framework import serializers
from course.models import Course, Pay
from lessons.models import Lesson
from lessons.serializers import LessonSerializer


class CourseSerializer(serializers.ModelSerializer):
    count_lessons = serializers.SerializerMethodField()
    list_of_lessons = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = "__all__"

    def get_count_lessons(self, instance):
        return Lesson.objects.filter(choice_course=instance).count()

    def get_list_of_lessons(self, v):
        list_lessons = [{"number": lesson.pk, "name": lesson.name}
                        for lesson in Lesson.objects.filter(choice_course=instance)]

        return list_lessons


class PaySerializer(serializers.ModelSerializer):
    course = serializers.PrimaryKeyRelatedField(read_only=True)
    lesson = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Pay
        fields = "__all__"
