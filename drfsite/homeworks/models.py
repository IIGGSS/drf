from django.db import models
from students.models import Student
from tutors.models import Tutor
# Create your models here.

class Homework(models.Model):
    student = models.ForeignKey(to=Student,on_delete=models.CASCADE,null=True, verbose_name="Ученик")
    tutor = models.ForeignKey(to=Tutor,on_delete=models.CASCADE,null=True, verbose_name="Репетитор")
    start_date = models.DateTimeField(verbose_name="Дата начала")
    end_date = models.DateTimeField(verbose_name="Дата конца")
    theme = models.CharField(max_length=30, verbose_name="Тема")
    description = models.CharField(max_length=30, verbose_name="Описание")
    
    def __str__(self):
        return f"{self.tutor.full_name()}, {self.student.full_name()}, {self.theme}"

    class Meta:
        verbose_name = 'Домашнее задание'
        verbose_name_plural = 'Домашние задания'