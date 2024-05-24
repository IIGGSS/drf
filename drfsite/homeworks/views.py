from rest_framework import generics
from .models import *
from .serializers import *

# Create your views here.

class HomeworkAPIList(generics.ListCreateAPIView):
   queryset = Homework.objects.all()
   serializer_class = HomeworkSerializer
   filterset_fields = ['student','tutor','start_date','end_date','theme','description']
   ordering_fields = ['student','tutor','start_date','end_date','theme','description']

class HomeworkAPIDetail(generics.RetrieveUpdateDestroyAPIView):
   queryset = Homework.objects.all()
   serializer_class = HomeworkSerializer