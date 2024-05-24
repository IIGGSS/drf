from rest_framework import generics
from .models import *
from .serializers import *

# Create your views here.

class StudentAPIList(generics.ListCreateAPIView):
   queryset = Student.objects.all()
   serializer_class = StudentSerializer
   filterset_fields = ['first_name','last_name','middle_name','birthday','phone','email','grade','parent_fio','parent_phone']
   ordering_fields = ['first_name','last_name','middle_name','birthday','phone','email','grade','parent_fio','parent_phone']
 
class StudentAPIDetail(generics.RetrieveUpdateDestroyAPIView):
   queryset = Student.objects.all()
   serializer_class = StudentSerializer