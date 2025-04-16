from django.db import models


class EducationModule(models.Model):
    order_number = models.PositiveIntegerField(verbose_name="Порядковый номер")
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    is_published = models.BooleanField(default=False, verbose_name="Статус публикации")

    class Meta:
        ordering = ["order_number"]
        verbose_name = "Образовательный модуль"
        verbose_name_plural = "Образовательные модули"

    def __str__(self):
        return self.title
