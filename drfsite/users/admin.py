from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = [
        "login",
    ]
    fieldsets = (
        ("Логин", {"fields": ("password", "login")}),
        (
            "Права и разрешения",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "is_superuser",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "login",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
    search_fields = ["login"]
    ordering = ["id"]


admin.site.register(User, CustomUserAdmin)
