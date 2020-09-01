"""Kakkop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

from users.views import LoginView, RegisterView

API_PATH = "api/v1"
API_TITLE = "Kakkop API"
API_DESCRIPTION = "REST API for the Kakkop game scoring application."
VERSION = "1.0.0"

admin = [path("admin", admin.site.urls)]
api = [
    path(f"{API_PATH}/", include("users.urls")),
]
auth = [
    path("api-auth/", include("rest_framework.urls")),
    path(f"{API_PATH}/auth/login", LoginView.as_view(), name="login"),
    path(
        f"{API_PATH}/auth/register", RegisterView.as_view(), name="register",
    ),
]
docs = [
    path(
        f"{API_PATH}/schema",
        get_schema_view(
            title=API_TITLE, description=API_DESCRIPTION, version=VERSION
        ),
        name="openapi-schema",
    ),
    path(
        f"{API_PATH}/swagger-ui",
        TemplateView.as_view(
            template_name="swagger-ui.html",
            extra_context={"schema_url": "openapi-schema"},
        ),
        name="swagger-ui",
    ),
]

urlpatterns = admin + api + auth + docs
