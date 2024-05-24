from rest_framework import generics
from .models import *
from .serializers import *

# Create your views here.

class RegistrationForServiceAPIList(generics.ListCreateAPIView):
   queryset = RegistrationForService.objects.all()
   serializer_class = RegistrationForServiceSerializer
   filterset_fields = ['tutor','student','service','start_date','end_date','theme_of_lesson','additional_info','status']
   ordering_fields = ['tutor','student','service','start_date','end_date','theme_of_lesson','additional_info','status']

class RegistrationForServiceAPIDetail(generics.RetrieveUpdateDestroyAPIView):
   queryset = RegistrationForService.objects.all()
   serializer_class = RegistrationForServiceSerializer