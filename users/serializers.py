from rest_framework import serializers
from course.serializers import PaySerializer
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    payment_history = PaySerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ("id", "email", "payment_history")
