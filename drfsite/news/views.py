from rest_framework import generics
from .models import *
from .serializers import *

# Create your views here.
class NewsAPIList(generics.ListCreateAPIView):
   queryset = News.objects.all()
   serializer_class = NewsSerializer
   filterset_fields = ['title','short_description','description']
   ordering_fields = ['title','short_description','description']

class NewsAPIDetail(generics.RetrieveUpdateDestroyAPIView):
   queryset = News.objects.all()
   serializer_class = NewsSerializer