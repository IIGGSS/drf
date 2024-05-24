from rest_framework import generics
from .models import *
from .serializers import *
# Create your views here.

class UserAPIVList(generics.ListCreateAPIView):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   filterset_fields = ['login']

class UserAPIDetail(generics.RetrieveUpdateDestroyAPIView):
   queryset = User.objects.all()
   serializer_class = UserSerializer