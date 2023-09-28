from django.db import models

from users.models import NULLABLE


class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='lesson_photo', verbose_name='превью (картинка)', **NULLABLE)
    link = models.TextField(verbose_name='ссылка на видео')

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'

    def __str__(self):
        return f"{self.name} {self.link}"


