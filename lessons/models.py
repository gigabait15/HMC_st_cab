from django.db import models
from course.models import Course

NULLABLE = {'blank': True, 'null': True}


class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='lesson_photo', verbose_name='превью (картинка)', **NULLABLE)
    link = models.TextField(verbose_name='ссылка на видео', **NULLABLE)
    is_pay = models.BooleanField(default=False, verbose_name='оплаченный урок')

    choice_course = models.ForeignKey(Course, default=1, on_delete=models.CASCADE, related_name='lessons')

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
        permissions = [
            ("can_view_lesson", f"Can view lesson "),
            (f"can_update_lesson", f"Can update lesson"),
        ]

    def __str__(self):
        return f"{self.name} {self.link}"



