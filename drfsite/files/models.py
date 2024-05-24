from django.db import models
from news.models import News
# Create your models here.

class File(models.Model):
    news = models.ForeignKey(to=News,on_delete=models.CASCADE,null=True, verbose_name="Новость")
    name = models.CharField(max_length=20, verbose_name="Название")
    file = models.FileField(verbose_name="Файл",upload_to="news/files/")
    
    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'