from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from lessons.models import Lesson
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.moderator = User.objects.create_user(username='moderator', password='moderatorpassword')
        self.lesson_data = {
            'title': 'Test ',
            'description': 'Test Lesson',
            'link': 'link',
        }

    def test_lesson_list(self):
        """Тест на просмотр списка уроков"""
        response = self.client.get('/lessons/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_lesson_detail(self):
        """Тест на просмотр урока"""
        response = self.client.get(f'/lessons/{self.lesson.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_lesson_create(self):
        """Тест на созданеие урока"""
        self.client.force_authenticate(user=self.user)
        response = self.client.post('/lessons/create/',
                                    data=self.lesson_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_lesson_update(self):
        """Тест на изменение урока"""
        self.client.force_authenticate(user=self.user)
        response = self.client.put(f'/lessons/update/{self.lesson.id}/',
                                   data=self.lesson_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_lesson_delete(self):
        """Тест на удаление урока"""
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(f'/lessons/delete/{self.lesson.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)