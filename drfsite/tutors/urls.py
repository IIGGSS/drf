from django.urls import path

from tutors.views import TutorProfileUpdatePage


urlpatterns = [
    path("tutor-profile", TutorProfileUpdatePage.as_view(), name="tutor-profile"),
]
