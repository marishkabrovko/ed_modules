from rest_framework import serializers

from .models import EducationModule


class EducationModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationModule
        fields = "__all__"

    def validate_order_number(self, value):
        instance = self.instance
        qs = EducationModule.objects.filter(order_number=value)
        if instance:
            qs = qs.exclude(pk=instance.pk)
        if qs.exists():
            raise serializers.ValidationError(
                "Модуль с таким порядковым номером уже существует."
            )
        return value
