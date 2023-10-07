from django.db import models
from users.models import NULLABLE, User


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    image = models.ImageField(upload_to='lesson_photo', verbose_name='превью (картинка)',  **NULLABLE)
    description = models.TextField(verbose_name='описание')

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'

    def __str__(self):
        return f"{self.name} {self.description}"


