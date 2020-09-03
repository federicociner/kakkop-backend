from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

from users.views import LoginView, RegisterView

API_PATH = "api/v1"
API_TITLE = "Kakkop API"
API_DESCRIPTION = "REST API for the Kakkop game scoring application."
VERSION = "1.0.0"

admin = [path("admin/", admin.site.urls)]
api = [
    path(f"{API_PATH}/", include("api.urls")),
    path(f"{API_PATH}/", include("users.urls")),
]
auth = [
    path("api-auth/", include("rest_framework.urls")),
    path(f"{API_PATH}/auth/login/", LoginView.as_view(), name="login"),
    path(
        f"{API_PATH}/auth/register/", RegisterView.as_view(), name="register",
    ),
]
docs = [
    path(
        f"{API_PATH}/schema/",
        get_schema_view(
            title=API_TITLE, description=API_DESCRIPTION, version=VERSION
        ),
        name="openapi-schema",
    ),
    path(
        f"{API_PATH}/swagger-ui/",
        TemplateView.as_view(
            template_name="swagger-ui.html",
            extra_context={"schema_url": "openapi-schema"},
        ),
        name="swagger-ui",
    ),
]

urlpatterns = admin + api + auth + docs
