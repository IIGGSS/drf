from django.contrib import messages
from django.shortcuts import redirect, reverse
from django.views.generic import TemplateView
from rest_framework import generics
from django.contrib.auth import login, authenticate
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import UserRegistrationForm
from .models import *
from .serializers import *


# Create your views here.


class UserAPIVList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_fields = ["login"]


class UserAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRegistrationView(TemplateView):
    template_name = "users/user_registration.html"

    def post(self, request, *args, **kwargs):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("students-profile"))
        print(form.errors)
        return super().get(request, *args, **kwargs)


class UserLoginView(TemplateView):
    template_name = "users/user_authorization.html"

    def post(self, request, *args, **kwargs):
        user = authenticate(
            request, username=request.POST["login"], password=request.POST["password"]
        )
        if user is not None:
            login(request, user)
            return redirect(reverse("students-profile"))
        messages.add_message(
            request, messages.ERROR, message="Не правильный логин или пароль"
        )
        return redirect(reverse("users-login"))
