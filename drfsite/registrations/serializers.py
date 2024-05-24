from rest_framework import serializers
from .models import *

class RegistrationForServiceSerializer(serializers.ModelSerializer):
   
   class Meta:
      model = RegistrationForService
      fields = '__all__'