from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import BaseUser


class BaseUserAdmin(UserAdmin):
    model = BaseUser
    list_display = (
        "email",
        "first_name",
        "last_name",
        "is_superuser",
        "is_active",
    )
    list_filter = (
        "email",
        "first_name",
        "last_name",
        "is_superuser",
        "is_active",
    )
    fieldsets = (
        (None, {"fields": ("email", "password", "first_name", "last_name")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(BaseUser, BaseUserAdmin)
