from django.db import models
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    image = models.ImageField(upload_to='lesson_photo', verbose_name='превью (картинка)',  **NULLABLE)
    description = models.TextField(verbose_name='описание')
    is_pay = models.BooleanField(default=False, verbose_name='оплаченный курс')

    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='user', default=1)
    product_id = models.CharField(max_length=150, **NULLABLE)

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'

    def __str__(self):
        return f"{self.name} {self.description}"


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    subscribed = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'

    def __str__(self):
        return f"{self.user} {self.course}"

