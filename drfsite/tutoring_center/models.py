
import enum
from django.db import models
import uuid
# Create your models here.
class level_of_education(enum.Enum):
   preschooler = 'preschooler'
   schooler = 'schooler'
   student = 'student'
   other = 'other'

class status_of_registration(enum.Enum):
   free = 'free'
   busy = 'busy'
   confirmed = 'confirmed'
   completed = 'completed'
   
   
class User(models.Model):
    id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True,primary_key=True)
    login =  models.CharField(max_length=20)
    password = models.CharField(max_length=20)

 

class Tutor(models.Model):
    id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True,primary_key=True)
    user = models.ForeignKey('User',on_delete=models.CASCADE,default=None)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    birthday = models.DateField()
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    education = models.CharField(max_length=100)
    services = models.CharField(max_length=50)
    


class Student(models.Model):
    id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True,primary_key=True)
    user = models.ForeignKey('User',on_delete=models.CASCADE,default=None)
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
    user = models.ForeignKey('User',on_delete=models.CASCADE,default=None)
    


class Service(models.Model):
    id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True,primary_key=True)
    tutor = models.ForeignKey('Tutor',on_delete=models.CASCADE,default=None)
    subject = models.CharField(max_length=30)
    info_about_service = models.CharField(max_length=50)
    price = models.FloatField()
    level = models.CharField(max_length=15, choices=[(tag.name, tag.value) for tag in level_of_education])
 
class Subject(models.Model):
    id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True,primary_key=True)
    name = models.CharField(max_length=20)

class Registragtion_for_service(models.Model):
    id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True,primary_key=True)
    tutor = models.ForeignKey('Tutor',on_delete=models.CASCADE,default=None)
    student = models.ForeignKey('Student',on_delete=models.CASCADE,default=None)
    service = models.ForeignKey('Service',on_delete=models.CASCADE,default=None)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    theme_of_lesson = models.CharField(max_length=30)
    additional_info = models.CharField(max_length=30)
    status = models.CharField(max_length=15, choices=[(tag.name, tag.value) for tag in status_of_registration])


class Homework(models.Model):
    id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True,primary_key=True)
    student = models.ForeignKey('Student',on_delete=models.CASCADE,default=None)
    tutor = models.ForeignKey('Tutor',on_delete=models.CASCADE,default=None)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    theme = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    

    
class File(models.Model):
    id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True,primary_key=True)
    name = models.CharField(max_length=20)
    file = models.FileField()
    


class New(models.Model):
    id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True,primary_key=True)
    title = models.CharField(max_length=30)
    short_description = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    small_preview = models.ImageField()
    preview = models.ImageField()
    file = models.FileField(File)
    