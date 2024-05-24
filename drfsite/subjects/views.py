from rest_framework import generics
from .models import *
from .serializers import *

# Create your views here.

class SubjectAPIList(generics.ListCreateAPIView):
   queryset = Subject.objects.all()
   serializer_class = SubjectSerializer
   filterset_fields = ['name']

class SubjectAPIDetail(generics.RetrieveUpdateDestroyAPIView):
   queryset = Subject.objects.all()
   serializer_class = SubjectSerializer