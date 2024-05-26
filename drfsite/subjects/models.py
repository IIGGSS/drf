from django.db import models

# Create your models here.


class Subject(models.Model):
    name = models.CharField(max_length=20, verbose_name="Название")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предметы"
