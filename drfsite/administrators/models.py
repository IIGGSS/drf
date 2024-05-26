from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from users.models import User

# Create your models here.


class Administrator(models.Model):
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, null=True, verbose_name="Пользователь"
    )

    def __str__(self):
        return f"{self.user.login}"

    class Meta:
        verbose_name = "Администратор"
        verbose_name_plural = "Администраторы"


@receiver(pre_save, sender=Administrator)
def check_user_existence(sender, instance, **kwargs):
    if not instance.user:
        raise ValidationError("У Administrator должен быть указан связанный User.")
