from rest_framework import serializers
from course.models import Course, Subscription
# from course.services import payment_create
from lessons.models import Lesson, Pay
from lessons.serializers import LessonSerializer


class CourseSerializer(serializers.ModelSerializer):
    count_lessons = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True)
    # create_pay = serializers.SerializerMethodField()
    # receiving_payment = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_count_lessons(self, instance):
        return Lesson.objects.filter(choice_course=instance).count()

#     def get_create_pay(self, instance):
#         item = Pay.objects.get(course=instance)
#         payment_intent = payment_create(
#             card_number=item.card_number,
#             expiration_date=item.expiration_date,
#             cvc=item.cvc,
#             payment_amount=item.payment_amount
#         )
#
#         Pay.objects.create(
#             course=instance,
#             card_number=item.card_number,
#             expiration_date=item.expiration_date,
#             cvc=item.cvc,
#         )
#         return payment_intent
#
# def get_receiving_payment(self, instance):
#         return None


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

