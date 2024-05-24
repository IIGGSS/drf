from rest_framework import generics
from .models import *
from .serializers import *

class TutorAPIList(generics.ListCreateAPIView):
   queryset = Tutor.objects.all()
   serializer_class = TutorSerializer
   filterset_fields = ['first_name','last_name','middle_name','birthday','phone','email','education']
   ordering_fields = ['first_name','last_name','middle_name','birthday','phone','email','education']

class TutorAPIDetail(generics.RetrieveUpdateDestroyAPIView):
   queryset = Tutor.objects.all()
   serializer_class = TutorSerializer