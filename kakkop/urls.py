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
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

API_TITLE = "Blog API"
API_DESCRIPTION = "A web API for creating and editing blog posts."
schema_view = get_schema_view(
    title=API_TITLE, description=API_DESCRIPTION, version="1.0.0"
)

admin = [path("admin/", admin.site.urls)]
api = [
    path("api/v1/", include("posts.urls")),
    path("api/v1/", include("users.urls")),
]
auth = [
    path("api-auth/", include("rest_framework.urls")),
    path(
        "api/v1/token/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path(
        "api/v1/token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh",
    ),
]
docs = [
    path("schema/", schema_view, name="openapi-schema"),
    path(
        "swagger-ui/",
        TemplateView.as_view(
            template_name="swagger-ui.html",
            extra_context={"schema_url": "openapi-schema"},
        ),
        name="swagger-ui",
    ),
]

urlpatterns = admin + api + auth + docs
