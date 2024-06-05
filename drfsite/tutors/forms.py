from django.forms import ModelForm

from tutors.models import Tutor


class TutorUpdateProfileForm(ModelForm):
    class Meta:
        model = Tutor
        fields = [
            "first_name",
            "last_name",
            "middle_name",
            "education",
            "email",
            "phone",
            "birthday",
        ]
