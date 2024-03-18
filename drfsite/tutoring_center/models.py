import enum
from django.db import models
import uuid


# Create your models here.
class level_of_education(enum.Enum):
   preschooler = 'preschooler',
   scholar = 'scholar',
   student = 'student',
   other = 'other',

class status_of_registration(enum.Enum):
   free = 'free'
   busy = 'busy'
   confirmed = 'confirmed'
   completed = 'completed'
   
class EducationLevelChoices(models.TextChoices):
    PRESCHOOLER = "PRESCHOOLER", "Дошкольники"
    SCHOLAR = "SCHOLAR", "Школьники"
    STUDENT = "STUDENT", "Студенты"
    OTHER = "OTHER", "Другие"


class User(models.Model):
    id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True,primary_key=True)
    login =  models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.login}"


class Tutor(models.Model):
    id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True,primary_key=True)
    user = models.ForeignKey(to=User,related_name='User',on_delete=models.CASCADE,null=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    birthday = models.DateField()
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    education = models.CharField(max_length=100)
    
    def full_name(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"

    def __str__(self):
        return f"{self.full_name()}"
    
    class Meta:
        verbose_name = 'Репетитор'
        verbose_name_plural = 'Репетиторы'


class Student(models.Model):
    id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True,primary_key=True)
    user = models.ForeignKey('User',on_delete=models.CASCADE,null=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    birthday = models.DateField()
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    grade = models.CharField(max_length=100)
    parents_fio = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)


class Administrator(models.Model):
    id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True,primary_key=True)
    user = models.ForeignKey('User',on_delete=models.CASCADE,null=True)


class Service(models.Model):
    id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True,primary_key=True)
    tutor = models.ForeignKey(verbose_name="Репетитор",to=Tutor,related_name='services',on_delete=models.CASCADE,null=True)
    subject = models.ForeignKey('Subject',verbose_name="Предмет",on_delete=models.CASCADE,null=True)
    info_about_service = models.CharField(max_length=50,verbose_name="Описание")
    price = models.FloatField(verbose_name="Цена")
    level = models.CharField(max_length=15, choices=EducationLevelChoices.choices, verbose_name="Уровень")
    
    def __str__(self):
        return f"{self.tutor.full_name()}, {self.subject}"

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class Subject(models.Model):
    id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True,primary_key=True)
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'


class Registration_for_service(models.Model):
    id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True,primary_key=True)
    tutor = models.ForeignKey('Tutor',on_delete=models.CASCADE,null=True)
    student = models.ForeignKey('Student',on_delete=models.CASCADE,null=True)
    service = models.ForeignKey('Service',on_delete=models.CASCADE,null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    theme_of_lesson = models.CharField(max_length=30)
    additional_info = models.CharField(max_length=30)
    status = models.CharField(max_length=15, choices=[(tag.name, tag.value) for tag in status_of_registration])


class Homework(models.Model):
    id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True,primary_key=True)
    student = models.ForeignKey('Student',on_delete=models.CASCADE,null=True)
    tutor = models.ForeignKey('Tutor',on_delete=models.CASCADE,null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    theme = models.CharField(max_length=30)
    description = models.CharField(max_length=30)


class File(models.Model):
    id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True,primary_key=True)
    name = models.CharField(max_length=20)
    file = models.FileField()


class News(models.Model):
    id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True,primary_key=True)
    title = models.CharField(max_length=30)
    short_description = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    small_preview = models.ImageField()
    preview = models.ImageField()
    file = models.FileField(File)
    