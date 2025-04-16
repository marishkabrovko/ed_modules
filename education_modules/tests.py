from rest_framework import status
from rest_framework.test import APITestCase

from .models import EducationModule
from .serializers import EducationModuleSerializer


class EducationModulesViewSetTest(APITestCase):
    """Проверка на создание, изменение, удаление и получение списка образовательных модулей"""

    def setUp(self):
        self.module1 = EducationModule.objects.create(
            order_number=1,
            title="Образовательный модуль 1",
            description="Описание образовательного модуля 1",
            is_published=True,
        )
        self.module1 = EducationModule.objects.create(
            order_number=2,
            title="Образовательный модуль 2",
            description="Описание образовательного модуля 2",
            is_published=False,
        )

    def test_list_modules(self):
        url = "/education_modules/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            len(response.data), 2
        )  # Должно быты два образовательных модуля

    def test_create_module(self):
        url = "/education_modules/"
        data = {
            "order_number": 3,
            "title": "Новый образовательный модуль",
            "description": "Описание образовательного модуля 3",
            "is_published": True,
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
            "is_published": False,
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


class ModulesSerializerTest(APITestCase):
    """Проверка корректности обработки данных сериализатором"""

    def setUp(self):
        self.module = EducationModule.objects.create(
            order_number=1,
            title="Тестовый образовательный модуль 1",
            description="Тест образовательного модуля 1",
            is_published=True,
        )

    def test_serializer_valid_data(self):
        data = {
            "order_number": 2,
            "title": "Новый тестовый модуль",
            "description": "Описание нового тестового модуля",
            "is_published": False,
        }
        serializer = EducationModuleSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data["order_number"], 2)
        self.assertEqual(serializer.validated_data["title"], "Новый тестовый модуль")
        self.assertEqual(
            serializer.validated_data["description"], "Описание нового тестового модуля"
        )
        self.assertFalse(serializer.validated_data["is_published"])

    def test_serializer_invalid_data(self):
        invalid_data = {
            "order_number": -1,
            "title": "",
            "description": "Описание нового модуля",
        }
        serializer = EducationModuleSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("order_number", serializer.errors)
        self.assertIn("title", serializer.errors)

    def test_serializer_fields(self):
        serializer = EducationModuleSerializer(instance=self.module)
        data = serializer.data
        self.assertEqual(
            set(data.keys()),
            {"id", "order_number", "title", "description", "is_published"},
        )
