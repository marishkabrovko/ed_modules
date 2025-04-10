from rest_framework.test import APITestCase
from rest_framework import status
from .models import EducationModule
from .serializers import EducationModuleSerializer
from django.urls import reverse


class EducationModulesViewSetTest(APITestCase):
    def setUp(self):
        self.module1 = EducationModule.objects.create(
            order_number=1,
            title="Образовательный модуль 1",
            description="Описание образовательного модуля 1",
            is_published=True
        )
        self.module1 = EducationModule.objects.create(
            order_number=2,
            title="Образовательный модуль 2",
            description="Описание образовательного модуля 2",
            is_published=False
        )

    def test_list_modules(self):
        url = '/education_modules/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Должно быты два образовательных модуля

    def test_create_module(self):
        url = "/education_modules/"
        data = {
            "order_number": 3,
            "title": "Новый образовательный модуль",
            "description": "Описание образовательного модуля 3",
            "is_published": True
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(EducationModule.objects.count(), 3)

    def test_update_module(self):
        url = f"/education_modules/{self.module1.id}/"
        data = {
            "order_number": 1,
            "title": "Обновленный образовательный модуль",
            "description": "Обновленное описание образовательного модуля 1",
            "is_published": False
        }
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.module1.refresh_from_db()
        self.assertEqual(self.module1.title, "Обновленный образовательный модуль")
        self.assertFalse(self.module1.is_published)

    def test_delete_module(self):
        url = f"/education_modules/{self.module1.id}/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(EducationModule.objects.count(), 1)
