import enum
from django.db import models
import uuid
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError

class StatusOfRegistration(models.TextChoices):
   FREE = 'FREE', 'Свободно'
   BUSY = 'BUSY', 'Занято'
   CONFIRMED = 'CONFIRMED', 'Подтверждено'
   COMPLETED = 'COMPLETED', 'Завершено'
   
class EducationLevelChoices(models.TextChoices):
    PRESCHOOLER = "PRESCHOOLER", "Дошкольники"
    SCHOLAR = "SCHOLAR", "Школьники"
    STUDENT = "STUDENT", "Студенты"
    OTHER = "OTHER", "Другие"


class User(models.Model):
    id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True,primary_key=True)
    login =  models.CharField(max_length=20,verbose_name="Логин")
    password = models.CharField(max_length=20,verbose_name="Пароль")
    
    def __str__(self):
        return f"{self.login}"
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Tutor(models.Model):
    id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True,primary_key=True)
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


class Student(models.Model):
    id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True,primary_key=True)
    user = models.ForeignKey('User',on_delete=models.CASCADE,null=True,verbose_name="Пользователь")
    first_name = models.CharField(max_length=20,verbose_name="Имя")
    last_name = models.CharField(max_length=20,verbose_name="Фамилия")
    middle_name = models.CharField(max_length=20,verbose_name="Отчество")
    birthday = models.DateField(verbose_name="Дата рождения")
    email = models.CharField(max_length=30,verbose_name="Электронная почта")
    phone = models.CharField(max_length=15,verbose_name="Номер телефона")
    grade = models.CharField(max_length=15, choices=EducationLevelChoices.choices, verbose_name="Уровень образования")
    parent_fio = models.CharField(max_length=100,verbose_name="ФИО родителя", null=True)
    parent_phone = models.CharField(max_length=15,verbose_name="Номер телефона родителя", null=True)
    
    def full_name(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"

    def __str__(self):
        return f"{self.full_name()}"
    
    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'

@receiver(pre_save, sender=Student)
def check_user_existence(sender, instance, **kwargs):
    if not instance.user:
        raise ValidationError('У Student должен быть указан связанный User.')


class Administrator(models.Model):
    id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True,primary_key=True)
    user = models.ForeignKey('User',on_delete=models.CASCADE,null=True,verbose_name="Пользователь")
    
    def __str__(self):
        return f"{self.user.login}"
     
    class Meta:
        verbose_name = 'Администратор'
        verbose_name_plural = 'Администраторы'

@receiver(pre_save, sender=Administrator)
def check_user_existence(sender, instance, **kwargs):
    if not instance.user:
        raise ValidationError('У Administrator должен быть указан связанный User.')


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
    name = models.CharField(max_length=20, verbose_name="Название")
    
    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'


class RegistrationForService(models.Model):
    id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True,primary_key=True)
    tutor = models.ForeignKey('Tutor',on_delete=models.CASCADE,null=True, verbose_name="Репетитор")
    student = models.ForeignKey('Student',on_delete=models.CASCADE,null=True, verbose_name="Ученик")
    service = models.ForeignKey('Service',on_delete=models.CASCADE,null=True, verbose_name="Услуга")
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


class Homework(models.Model):
    id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True,primary_key=True)
    student = models.ForeignKey('Student',on_delete=models.CASCADE,null=True, verbose_name="Ученик")
    tutor = models.ForeignKey('Tutor',on_delete=models.CASCADE,null=True, verbose_name="Репетитор")
    start_date = models.DateTimeField(verbose_name="Дата начала")
    end_date = models.DateTimeField(verbose_name="Дата конца")
    theme = models.CharField(max_length=30, verbose_name="Тема")
    description = models.CharField(max_length=30, verbose_name="Описание")
    
    def __str__(self):
        return f"{self.tutor.full_name()}, {self.student.full_name()}, {self.theme}"

    class Meta:
        verbose_name = 'Домашнее задание'
        verbose_name_plural = 'Домашние задания'


class File(models.Model):
    id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True,primary_key=True)
    news = models.ForeignKey('News',on_delete=models.CASCADE,null=True, verbose_name="Новость")
    name = models.CharField(max_length=20, verbose_name="Название")
    file = models.FileField(verbose_name="Файл",upload_to="news/files/")
    
    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'


class News(models.Model):
    id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True,primary_key=True)
    title = models.CharField(max_length=30, verbose_name="Название")
    short_description = models.CharField(max_length=30, verbose_name="Краткое описание")
    description = models.TextField(verbose_name="Описание")
    small_preview = models.ImageField(verbose_name="Малое превью", blank=True, null=True)
    preview = models.ImageField(verbose_name="Превью", blank=True, null=True)
    
    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
    