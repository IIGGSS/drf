from django.db import models


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=30, verbose_name="Название")
    short_description = models.CharField(max_length=30, verbose_name="Краткое описание")
    description = models.TextField(verbose_name="Описание")
    small_preview = models.ImageField(
        verbose_name="Малое превью", blank=True, null=True
    )
    preview = models.ImageField(verbose_name="Превью", blank=True, null=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
