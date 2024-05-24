from rest_framework import serializers
from .models import *
from services.serializers import ServiceSerializer
class TutorSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True, read_only=True)
    class Meta:
       model = Tutor
       fields = '__all__'
