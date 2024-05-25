from django.contrib.auth.forms import UserCreationForm
from django.forms import forms

from users.models import User


class UserRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["login"]
