from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, reverse
from django.views.generic import TemplateView
from students.models import Student

from users.forms import UserRegistrationForm


class UserRegistrationView(TemplateView):
    template_name = "users/user_registration.html"

    def post(self, request, *args, **kwargs):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Student.objects.create(user=user)
            login(request, user)
            return redirect(reverse("service-list"))
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
            if not hasattr(user, "student"):
                return redirect(reverse("service-list"))
            return redirect(reverse("students-profile"))
        messages.add_message(
            request, messages.ERROR, message="Не правильный логин или пароль"
        )
        return redirect(reverse("login"))
