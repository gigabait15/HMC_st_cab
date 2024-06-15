from rest_framework import serializers
from course.models import Course, Subscription
from course.services import product_create, product_list, price_create, price_list, session_create, session_list
from lessons.models import Lesson
from lessons.serializers import LessonSerializer


class CourseSerializer(serializers.ModelSerializer):
    count_lessons = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)
    create_product = serializers.SerializerMethodField()
    create_price = serializers.SerializerMethodField()
    create_session = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_create_session(self, instance):
        request_method = self.context['request'].method
        session_id = None
        session_url = None

        if request_method == 'POST':
            session_id = session_create(instance.id)
            if session_id:
                session_url = session_list(session_id)
                print(f'session_url {session_url}')
                return f"ссылка на оплату: {session_url}"
        elif request_method == 'GET':
            session_id = session_create(instance.id)
            print(f'session_id from context: {session_id}')
            if session_id:
                session_url = session_list(session_id)
                print(f'session_url {session_url}')
                return f"ссылка на оплату: {session_url}"

        return None

    @staticmethod
    def get_count_lessons(instance):
        lesson_count = Lesson.objects.filter(choice_course=instance).count()
        if instance.lesson_count != lesson_count:
            instance.lesson_count = lesson_count
            instance.save()
        return lesson_count

    def get_create_price(self, instance):
        request_method = self.context['request'].method
        price = None

        if request_method == 'POST':
            price = price_create(instance.id)
        elif request_method == 'GET':
            price = price_list(instance.id)

            # Подробное отладочное сообщение
            # print(f'Request method: {request_method}')
            # print(f'Product received: {price}')
            # print(f'Product type: {type(price)}')

            if price:
                price = price[0]
                # Проверяем наличие необходимых атрибутов
                price_id = price.get('id', None)
                price_name = price.get('nickname', None)
                product_id = price.get('product', None)
                print(f'price ID: {price_id}')
                print(f'price name: {price_name}')
                print(f'product id: {product_id}')

                if price_id and price_name:
                    return {
                        "id": price_id,
                        "name": price_name,
                        "product_id": product_id,
                    }
                else:
                    raise AttributeError('Объект цены не имеет необходимых атрибутов')
            return {}

    def get_create_product(self, instance):
        request_method = self.context['request'].method
        product = None

        if request_method == 'POST':
            product = product_create(instance.id)
            self.get_create_price(instance)
            self.get_create_session(instance)
        elif request_method == 'GET':
            product = product_list(instance.id)
            self.get_create_price(instance)

        # Подробное отладочное сообщение
        # print(f'Request method: {request_method}')
        # print(f'Product received: {product}')
        # print(f'Product type: {type(product)}')

        if product:
            # Проверяем наличие необходимых атрибутов
            product_id = product.get('id', None)
            product_name = product.get('name', None)
            print(f'Product ID: {product_id}')
            print(f'Product Name: {product_name}')

            if product_id and product_name:
                return {
                    "id": product_id,
                    "name": product_name,
                }
            else:
                raise AttributeError('Объект продукта не имеет необходимых атрибутов')
        return {}
#
#         Pay.objects.create(
#             course=instance,
#             card_number=item.card_number,
#             expiration_date=item.expiration_date,
#             cvc=item.cvc,
#         )
#         return product_intent
#
# def get_receiving_product(self, instance):
#         return None


class SubscriptionSerializer(serializers.ModelSerializer):
    subscribed = serializers.BooleanField()

    class Meta:
        model = Subscription
        fields = "__all__"

    def create(self, validated_data):
        user = self.context['request'].user
        subscribed = validated_data.get('subscribed', False)
        course = validated_data.get('course')

        subscription, created = Subscription.objects.get_or_create(
            user=user,
            course=course,
            defaults={'subscribed': subscribed}
        )

        if not created:
            subscription.subscribed = subscribed
            subscription.save()

        return subscription