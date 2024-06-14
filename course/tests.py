from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from users.models import User


def create_user(new_email: str, new_password: str):
    user = User.objects.create(
        email=new_email,
        first_name='',
        last_name='',
        is_staff=True,
        is_superuser=True
    )

    user.set_password(new_password)
    user.save()
    return user

class CourseSubscriptionTestCase(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = create_user('Test', '1234')
        self.client.force_authenticate(user=self.user)

    def test_course_sub(self):
        """функционал работы подписки на обновления курса"""
        data = {
            'user': 'test',
            'course': 'test',
            'subscribed': True
        }
        response = self.client.post(
            '/course/subscription/create/',
            data=data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )
