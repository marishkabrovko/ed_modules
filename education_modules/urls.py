from rest_framework.routers import DefaultRouter
from .apps import EducationModulesConfig
from .views import EducationModuleViewSet

app_name = EducationModulesConfig.name

router = DefaultRouter()
router.register(r"education_modules", EducationModuleViewSet, basename="education_modules")

urlpatterns = [
] + router.urls
