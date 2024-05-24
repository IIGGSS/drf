from rest_framework import generics
from .models import *
from .serializers import *
# Create your views here.

class AdministratorAPIList(generics.ListCreateAPIView):
   queryset = Administrator.objects.all()
   serializer_class = AdministratorSerializer

class AdministratorAPIDetail(generics.RetrieveUpdateDestroyAPIView):
   queryset = Administrator.objects.all()
   serializer_class = AdministratorSerializer