from django.shortcuts import redirect, reverse
from django.views.generic import UpdateView, DetailView
from rest_framework import generics

from .forms import StudentUpdateForm
from .models import *
from .serializers import *

# Create your views here.


class StudentAPIList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filterset_fields = [
        "first_name",
        "last_name",
        "middle_name",
        "birthday",
        "phone",
        "email",
        "grade",
        "parent_fio",
        "parent_phone",
    ]
    ordering_fields = [
        "first_name",
        "last_name",
        "middle_name",
        "birthday",
        "phone",
        "email",
        "grade",
        "parent_fio",
        "parent_phone",
    ]


class StudentAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentUpdatePage(UpdateView):
    queryset = Student.objects.all()
    form_class = StudentUpdateForm
    template_name = "students/student-update.html"

    def get_success_url(self):
        return reverse("students-profile")

    def get_object(self, queryset=None):
        return self.request.user.student


class StudentViewPage(DetailView):
    queryset = Student.objects.all()
    template_name = "students/student-view.html"
