from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.utils.timezone import now
from lessons.models import Lesson

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')

    phone = models.CharField(max_length=40, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='Страна', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

class Pay(models.Model):
    PAYMENT_METHOD = (
        (1, 'наличные'),
        (2, 'перевод')
    )
    PAID = (
        (1, 'оплачен курс'),
        (2, 'оплачен урок'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE, related_name='pays')
    course = models.ForeignKey('course.Course', on_delete=models.CASCADE, **NULLABLE, related_name='course')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, **NULLABLE, related_name='lesson')

    date_of_payment = models.DateField(verbose_name='дата оплаты', default=now)
    is_paid = models.IntegerField(verbose_name='оплаченный курс или урок', choices=PAID)
    payment_amount = models.PositiveIntegerField(verbose_name='сумма оплаты')
    payment_method = models.IntegerField(verbose_name='способ оплаты', choices=PAYMENT_METHOD, default=2)
    # card_number = models.CharField(default=1111111111111111, verbose_name='Номер кредитной карты')
    # expiration_date = models.CharField(default='11/1111', max_length=7, validators=[
    #     RegexValidator(regex=r'^\d{2}/\d{4}$', message="Формат даты должен быть 'MM/YYYY'", )],
    #                                    verbose_name='Дата окончания срока действия кредитной карты')
    # cvc = models.CharField(default=111, verbose_name='Код проверки карты')

    class Meta:
        verbose_name = 'оплата'
        verbose_name_plural = 'оплаты'

    def __str__(self):
        return f"{self.user} - {self.course if self.course else self.lesson} - {self.date_of_payment}"

    def save(self, *args, **kwargs):
        if self.payment_amount > 0:
            self.is_paid = True
        super().save(*args, **kwargs)