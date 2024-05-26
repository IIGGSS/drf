from django import forms

from students.models import Student


class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        exclude = ["user"]
