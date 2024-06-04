from django.shortcuts import reverse
from django.views.generic import UpdateView

from tutors.forms import TutorUpdateProfileForm
from tutors.models import Tutor


class TutorProfileUpdatePage(UpdateView):
    queryset = Tutor.objects.all()
    form_class = TutorUpdateProfileForm
    template_name = "tutors/tutor_profile.html"

    def get_object(self, queryset=None):
        return self.request.user.tutor

    def get_success_url(self):
        return reverse("tutor-profile")
