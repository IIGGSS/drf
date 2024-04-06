from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
   class Meta:
      model = User
      fields = '__all__'
      

class ServiceSerializer(serializers.ModelSerializer):
   class Meta:
      model = Service
      fields = '__all__'

class TutorSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True, read_only=True)
    class Meta:
       model = Tutor
       fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
   
   class Meta:
      model = Student
      fields = '__all__'


class AdministratorSerializer(serializers.ModelSerializer):
   
   class Meta:
      model = Administrator
      fields = '__all__'


class SubjectSerializer(serializers.ModelSerializer):
   
   class Meta:
      model = Subject
      fields = '__all__'


class RegistrationForServiceSerializer(serializers.ModelSerializer):
   
   class Meta:
      model = RegistrationForService
      fields = '__all__'


class HomeworkSerializer(serializers.ModelSerializer):
   
   class Meta:
      model = Homework
      fields = '__all__'


class FileSerializer(serializers.ModelSerializer):
   
   class Meta:
      model = File
      fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
   
   class Meta:
      model = News
      fields = '__all__'


