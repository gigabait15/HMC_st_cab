from django.db import models
from django.utils import timezone
from users.models import NULLABLE, User


class Pay(models.Model):
    PAYMENT_METHOD = (
        (1, 'наличные'),
        (2, 'перевод на счет')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE, related_name='user')

    date_of_payment = models.DateField(verbose_name='дата оплаты', default=timezone.now())
    payment_amount = models.PositiveIntegerField(verbose_name='сумма оплаты')
    payment_method = models.IntegerField(verbose_name='способ оплаты', choices=PAYMENT_METHOD, default=2)
    is_paid = models.BooleanField(verbose_name='оплачено', default=False)

    class Meta:
        verbose_name = 'оплата'
        verbose_name_plural = 'оплаты'

    def __str__(self):
        return f"{self.user}: {self.is_paid}"

    def save(self, *args, **kwargs):
        if self.payment_amount > 0:
            self.is_paid = True
        super().save(*args, **kwargs)


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    image = models.ImageField(upload_to='lesson_photo', verbose_name='превью (картинка)',  **NULLABLE)
    description = models.TextField(verbose_name='описание')

    paid_course = models.ForeignKey(Pay, on_delete=models.CASCADE, **NULLABLE, related_name='pay_course')

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'

    def __str__(self):
        return f"{self.name} {self.description}"


