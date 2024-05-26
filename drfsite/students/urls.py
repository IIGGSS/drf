from django.urls import path
from .views import StudentUpdatePage, StudentViewPage

urlpatterns = [
    path("profile/", StudentUpdatePage.as_view(), name="students-profile"),
    path(
        "students-view-profile/<pk>",
        StudentViewPage.as_view(),
        name="students-view-profile",
    ),
]
