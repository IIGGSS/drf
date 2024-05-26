from django.db import models
from students.models import EducationLevelChoices
from tutors.models import Tutor
from subjects.models import Subject

# Create your models here.


class Service(models.Model):
    tutor = models.ForeignKey(
        verbose_name="Репетитор",
        to=Tutor,
        related_name="services",
        on_delete=models.CASCADE,
        null=True,
    )
    subject = models.ForeignKey(
        to=Subject, verbose_name="Предмет", on_delete=models.CASCADE, null=True
    )
    info_about_service = models.TextField(verbose_name="Описание")
    price = models.FloatField(verbose_name="Цена")
    level = models.CharField(
        max_length=15, choices=EducationLevelChoices.choices, verbose_name="Уровень"
    )

    @property
    def free_slots(self):
        return self.slots.filter(student=None)

    def __str__(self):
        return f"{self.tutor.full_name()}, {self.subject}"

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"


class ServiceSlot(models.Model):
    service = models.ForeignKey(Service, on_delete=models.PROTECT, related_name="slots")
    start_time = models.DateTimeField("Дата и время старта")
    duration = models.IntegerField("Продолжительность (минуты)")
    student = models.ForeignKey(
        "students.Student",
        on_delete=models.PROTECT,
        related_name="slots",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Слот услуги"
        verbose_name_plural = "Слоты услуг"
        ordering = ["start_time"]
