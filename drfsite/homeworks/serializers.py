from rest_framework import serializers
from .models import *

class HomeworkSerializer(serializers.ModelSerializer):
   
   class Meta:
      model = Homework
      fields = '__all__'