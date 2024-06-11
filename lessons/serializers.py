from rest_framework import serializers
from lessons.models import Lesson
from lessons.validators import LinkValidator


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [LinkValidator(field='link')]
