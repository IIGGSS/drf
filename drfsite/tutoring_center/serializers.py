from rest_framework import serializers
from .models import *


class ServiceSerializer(serializers.ModelSerializer):
   class Meta:
      model = Service
      exclude = ["tutor"]


class TutorSerializer(serializers.ModelSerializer):
   services = ServiceSerializer(read_only=True, many=True)
   
   class Meta:
      model = Tutor
      fields = '__all__'