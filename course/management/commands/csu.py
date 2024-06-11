from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    help = 'создание пользователя'

    def handle(self, *args, **options):
        email_admin = 'test@gmail.com'

        # Проверяем, существует ли уже пользователь с email 'admin'
        if not User.objects.filter(email=email_admin).exists():
            admin = User.objects.create(
                email=email_admin,
                is_staff=True,
                # is_superuser=True,
                is_active=True
            )
            admin.set_password('1234')  # Устанавливаем пароль для администратора
            admin.save()
            self.stdout.write(self.style.SUCCESS(f'Пользователь {admin.email} создан'))
        else:
            self.stdout.write(self.style.WARNING(f'Пользователь с email {email_admin} уже существует'))
