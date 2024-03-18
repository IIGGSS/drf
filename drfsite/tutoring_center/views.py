from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *


class TutorAPIView(generics.ListAPIView):
   queryset = Tutor.objects.all()
   serializer_class = TutorSerializer