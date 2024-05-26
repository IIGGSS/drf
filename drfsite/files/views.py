from rest_framework import generics
from .models import *
from .serializers import *


# Create your views here.
class FileAPIList(generics.ListCreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    filterset_fields = ["news", "name"]
    ordering_fields = ["news", "name"]


class FileAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
