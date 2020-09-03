from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class BaseUserManager(BaseUserManager):
    """Custom user model manager, where email is the unique identifier for
    authentication instead of username.

    """

    def create_user(
        self, email, first_name, last_name, password, **extra_fields
    ):
        if not email:
            raise ValueError(_("Email address is a required field."))

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            **extra_fields
        )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(
        self, email, first_name, last_name, password, **extra_fields
    ):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))

        return self.create_user(
            email, first_name, last_name, password, **extra_fields
        )
