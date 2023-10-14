import requests
from rest_framework import status
import stripe
from stripe import PaymentIntent
from config import settings


def payment_create(card_number, expiration_date, cvc, payment_amount):
    """
       :param card_number: Номер кредитной карты (16 цифр).
       :param expiration_date: Дата окончания срока действия (MM/YY).
       :param cvc: Код проверки карты (3 цифры).
       :param payment_amount: Сумма платежа.
       """
    stripe.api_key = settings.API_KEY
    payment_intent = stripe.PaymentIntent.create(
        amount=payment_amount,
        currency="usd",
        payment_method_types=['card'],
        card={
            "number": card_number,
            "exp_month": expiration_date[:2],
            "exp_year": expiration_date[3:],
            "cvc": cvc,
        }
    )
    return payment_intent


