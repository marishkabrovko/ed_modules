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


