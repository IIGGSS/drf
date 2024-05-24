from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from users.models import User
# Create your models here.

class Tutor(models.Model):
    user = models.ForeignKey(to=User,related_name='User',on_delete=models.CASCADE,null=True,verbose_name="Пользователь")
    first_name = models.CharField(max_length=20,verbose_name="Имя")
    last_name = models.CharField(max_length=20,verbose_name="Фамилия")
    middle_name = models.CharField(max_length=20,verbose_name="Отчество")
    birthday = models.DateField(verbose_name="Дата рождения")
    email = models.CharField(max_length=30,verbose_name="Электронная почта")
    phone = models.CharField(max_length=15,verbose_name="Номер телефона")
    education = models.TextField(max_length=255,verbose_name="Образование")
    
    def full_name(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"

    def __str__(self):
        return f"{self.full_name()}"
    
    class Meta:
        verbose_name = 'Репетитор'
        verbose_name_plural = 'Репетиторы'

@receiver(pre_save, sender=Tutor)
def check_user_existence(sender, instance, **kwargs):
    if not instance.user:
        raise ValidationError('У Tutor должен быть указан связанный User.')
