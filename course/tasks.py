from celery import shared_task
from django.core.mail import send_mail
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from config.settings import EMAIL_HOST_USER
from course.models import Course
from lessons.models import Lesson


@shared_task
def update_course_lesson_count(course_id):
    try:
        course = Course.objects.get(id=course_id)
        lesson_count = Lesson.objects.filter(choice_course=course).count()
        if course.lesson_count != lesson_count:
            old_lesson_count = course.lesson_count
            course.lesson_count = lesson_count
            course.save()

            # Отправка уведомления по электронной почте
            send_mail(
                'Изменение количества уроков в курсе',
                f'Количество уроков в курсе "{course.name}" '
                        f'было изменено с {old_lesson_count} на {lesson_count}.',
                f'{EMAIL_HOST_USER}',
                [course.user],
                fail_silently=False,
            )
    except Course.DoesNotExist:
        pass

@receiver(post_save, sender=Lesson)
@receiver(post_delete, sender=Lesson)
def update_course_lesson_count_signal(sender, instance, **kwargs):
    update_course_lesson_count.delay(instance.choice_course_id)