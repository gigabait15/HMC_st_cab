from rest_framework import serializers
from lessons.models import Lesson, Pay
from lessons.validators import LinkValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"

class LessonCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [LinkValidator(field='link')]


class PaySerializer(serializers.ModelSerializer):
    course = serializers.PrimaryKeyRelatedField(read_only=True)
    lesson = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Pay
        fields = "__all__"