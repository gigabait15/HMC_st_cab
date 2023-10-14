from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone
from course.models import Course
from users.models import NULLABLE, User


class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='lesson_photo', verbose_name='превью (картинка)', **NULLABLE)
    link = models.TextField(verbose_name='ссылка на видео')

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    choice_course = models.ForeignKey(Course, default=1, on_delete=models.CASCADE, related_name='lessons')

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'

    def __str__(self):
        return f"{self.name} {self.link}"


class Pay(models.Model):
    PAYMENT_METHOD = (
        (1, 'наличные'),
        (2, 'перевод на счет')
    )
    PAID = (
        (1, 'оплачен курс'),
        (2, 'оплачен урок'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE, related_name='pay')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE, related_name='pay')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, **NULLABLE, related_name='pay')

    date_of_payment = models.DateField(verbose_name='дата оплаты', default=timezone.now())
    is_paid = models.IntegerField(verbose_name='оплаченный курс или урок', choices=PAID)
    payment_amount = models.PositiveIntegerField(verbose_name='сумма оплаты')
    payment_method = models.IntegerField(verbose_name='способ оплаты', choices=PAYMENT_METHOD, default=2)
    card_number = models.CharField(default=1111111111111111, verbose_name='Номер кредитной карты')
    expiration_date = models.CharField(default='11/1111', max_length=7, validators=[
        RegexValidator(regex=r'^\d{2}/\d{4}$', message="Формат даты должен быть 'MM/YYYY'", )],
                                       verbose_name='Дата окончания срока действия кредитной карты')
    cvc = models.CharField(default=111, verbose_name='Код проверки карты')

    class Meta:
        verbose_name = 'оплата'
        verbose_name_plural = 'оплаты'

    def __str__(self):
        user = self.user.username if self.user else "N/A"
        course_or_lesson = ""
        if self.is_paid == 1:
            course_or_lesson = f"Курс: {self.course}"
        elif self.is_paid == 2:
            course_or_lesson = f"Урок: {self.lesson}"

        return f"Пользователь: {user}, {course_or_lesson}"

    def save(self, *args, **kwargs):
        if self.payment_amount > 0:
            self.is_paid = True
        super().save(*args, **kwargs)
