from rest_framework import generics
from .models import *
from .serializers import *
# Create your views here.

class ServiceAPIList(generics.ListCreateAPIView):
   queryset = Service.objects.all()
   serializer_class = ServiceSerializer
   filterset_fields = ['tutor','info_about_service','subject','price','level']
   ordering_fields = ['tutor','info_about_service','subject','price','level']
   
class ServiceAPIDetail(generics.RetrieveUpdateDestroyAPIView):
   queryset = Service.objects.all()
   serializer_class = ServiceSerializer