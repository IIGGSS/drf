from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    # django apps
    path("", include("news.urls")),
    path("users/", include("users.urls")),
    path("students/", include("students.urls")),
    path("services/", include("services.urls")),
]
