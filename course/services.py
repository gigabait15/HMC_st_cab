import stripe
from config import settings
from course.models import Course
from users.models import Pay

stripe.api_key = settings.API_KEY


def product_create(course_id):
    """Создание продукта и привязка к курсу"""
    course = Course.objects.get(id=course_id)
    if course.product_id:
        print(f'Продукт уже создан для Course_id: {course_id}')
        return stripe.Product.retrieve(course.product_id)

    try:
        product_intent = stripe.Product.create(
            name=course.name,
            active=True,
            description=course.description,
        )
        course.product_id = product_intent.id
        course.save()
        return product_intent
    except stripe.error.InvalidRequestError as e:
        # Логирование ошибки
        print(f'Ошибка при создании продукта: {e}')
        raise e

def product_list(course_id):
    """Просмотр продукта"""
    course = Course.objects.get(id=course_id)
    if not course.product_id:
        print(f'Нет продукта, связанного с Course_id: {course_id}')
        return None

    try:
        product = stripe.Product.retrieve(course.product_id)
        return product
    except stripe.error.InvalidRequestError as e:
        # Логирование ошибки
        print(f'Ошибка при получении продукта: {e}')
        raise e

def price_create(course_id):
    """Создание цены"""
    course = Course.objects.get(id=course_id)
    if not course.product_id:
        print(f'Нет продукта, связанного с Course_id: {course_id}')
        return None

    try:
        price = stripe.Price.create(
            currency="rub",
            unit_amount=10000,
            recurring={"interval": "month"},
            product=course.product_id,
            nickname=f"цена платежа для курса {course.name}",
        )
        return price

    except stripe.error.InvalidRequestError as e:
        # Логирование ошибки
        print(f'Ошибка при создании цены: {e}')
        raise e

def price_list(course_id):
    """Просмотр цены"""
    course = Course.objects.get(id=course_id)
    if not course.product_id:
        print(f'Нет цены, связанного с Course_id: {course_id}')
        return None

    try:
        price = stripe.Price.list(product=course.product_id)
        return price.data
    except stripe.error.InvalidRequestError as e:
        # Логирование ошибки
        print(f'Ошибка при получении цены: {e}')
        raise e

def session_create(course_id):
    """Создание сессии для оплаты"""
    course = Course.objects.get(id=course_id)
    prices = price_list(course_id)
    if not prices:
        print(f'Нет доступных цен для Course_id: {course_id}')
        return None

    price_id = prices[0]['id']  # Получаем идентификатор первой цены

    try:
        session = stripe.checkout.Session.create(
            success_url="http://127.0.0.1:8000/success",
            line_items=[{"price": price_id, "quantity": 2}],
            mode="subscription",
        )
        return session.id
    except stripe.error.InvalidRequestError as e:
        # Логирование ошибки
        print(f'Ошибка при создании сессии: {e}')
        raise e

def session_list(session_id):
    """Просмотр сессии для оплаты"""
    try:
        session = stripe.checkout.Session.retrieve(session_id)
        return session.url
    except stripe.error.InvalidRequestError as e:
        # Логирование ошибки
        print(f'Ошибка при получении сессии: {e}')
        raise e