from django.db import models
from course.models import Course, Pay
from users.models import NULLABLE


class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='lesson_photo', verbose_name='превью (картинка)', **NULLABLE)
    link = models.TextField(verbose_name='ссылка на видео')

    paid_lesson = models.ForeignKey(Pay, on_delete=models.CASCADE, **NULLABLE, related_name='pay_lesson')
    choice_course = models.ForeignKey(Course, default=1, on_delete=models.CASCADE, related_name='course')

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'

    def __str__(self):
        return f"{self.name} {self.link}"


