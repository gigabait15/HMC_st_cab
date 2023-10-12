from django.core.management import BaseCommand
from users.models import User

class UserCommand(BaseCommand):
    help = 'создание пользователя'

    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@admin.ru',
            first_name='Admin',
            last_name='Admin',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('Admin')
        user.save()

        self.stdout.write(self.style.SUCCESS('Пользователь создан'))

        return user