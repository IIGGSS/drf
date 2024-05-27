from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    # django apps
    path("", include("news.urls")),
    path("users/", include("users.urls")),
    path("students/", include("students.urls")),
    path("services/", include("services.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
