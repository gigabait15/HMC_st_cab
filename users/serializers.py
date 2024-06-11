from rest_framework import serializers
from users.models import *


class PaySerializer(serializers.ModelSerializer):

    class Meta:
        model = Pay
        fields = '__all__'


class PublicUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', )

class PrivateUserSerializer(serializers.ModelSerializer):
    pays = PaySerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'pays')

    def get_pay(self, instance):
        return Pay.objects.all()

