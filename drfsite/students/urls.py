from django.urls import path
from .views import StudentUpdatePage

urlpatterns = [
    path("profile/", StudentUpdatePage.as_view(), name="students-profile"),
]
