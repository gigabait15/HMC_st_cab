from rest_framework import serializers
from course.models import Course, Subscription
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


class SubscriptionSerializer(serializers.ModelSerializer):
    subscribed = serializers.SerializerMethodField()
    class Meta:
        model = Subscription
        fields = '__all__'

    def get_subscribed(self, obj):
        request = self.context.get('request')
        if request.user.is_authenticated:
            user = request.user
            try:
                subscription = Subscription.objects.get(user=user, course=obj)
                return subscription.subscribed
            except Subscription.DoesNotExist:
                return False
        return False

