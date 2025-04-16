from rest_framework import viewsets

from .models import EducationModule
from .serializers import EducationModuleSerializer


class EducationModuleViewSet(viewsets.ModelViewSet):
    queryset = EducationModule.objects.all()
    serializer_class = EducationModuleSerializer
