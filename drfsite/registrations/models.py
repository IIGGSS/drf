from django.db import models
from tutors.models import Tutor
from students.models import Student
from services.models import Service
# Create your models here.

class StatusOfRegistration(models.TextChoices):
   FREE = 'FREE', 'Свободно'
   BUSY = 'BUSY', 'Занято'
   CONFIRMED = 'CONFIRMED', 'Подтверждено'
   COMPLETED = 'COMPLETED', 'Завершено'


class RegistrationForService(models.Model):
    tutor = models.ForeignKey(to=Tutor,on_delete=models.CASCADE,null=True, verbose_name="Репетитор")
    student = models.ForeignKey(to=Student,on_delete=models.CASCADE,null=True, verbose_name="Ученик")
    service = models.ForeignKey(to=Service,on_delete=models.CASCADE,null=True, verbose_name="Услуга")
    start_date = models.DateTimeField(verbose_name="Дата начала")
    end_date = models.DateTimeField(verbose_name="Дата конца")
    theme_of_lesson = models.CharField(max_length=30, verbose_name="Тема урока")
    additional_info = models.CharField(max_length=30, verbose_name="Дополнительная информация")
    status = models.CharField(max_length=15, choices=StatusOfRegistration.choices,verbose_name="Статус")
    
    def __str__(self):
        return f"{self.tutor.full_name()}, {self.student.full_name()}, {self.service.subject.name}"

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'