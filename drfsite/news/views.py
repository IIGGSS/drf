from django.views.generic import TemplateView
from rest_framework import generics

from tutors.models import Tutor
from .models import *
from .serializers import *


# Create your views here.
class NewsAPIList(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filterset_fields = ["title", "short_description", "description"]
    ordering_fields = ["title", "short_description", "description"]


class NewsAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class IndexPageView(TemplateView):
    template_name = "news/index.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["tutors"] = Tutor.objects.all()
        return data


class AboutPageView(TemplateView):
    template_name = "news/about.html"
