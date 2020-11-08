from django.contrib import admin
from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from graphene_django.views import GraphQLView
from rest_framework.schemas import get_schema_view

from users.views import LoginView, RegisterView

API_TITLE = "Kakkop API"
API_DESCRIPTION = "REST API for the Kakkop game scoring application."
VERSION = "1.0.0"

admin = [path("admin/", admin.site.urls, name="admin")]
auth = [
    path("users/", include("users.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path("auth/login/", LoginView.as_view(), name="login"),
    path("auth/register/", RegisterView.as_view(), name="register"),
]
docs = [
    path(
        "schema/",
        get_schema_view(title=API_TITLE, description=API_DESCRIPTION, version=VERSION),
        name="openapi-schema",
    ),
    path(
        "swagger-ui/",
        TemplateView.as_view(
            template_name="swagger-ui.html",
            extra_context={"schema_url": "openapi-schema"},
        ),
        name="swagger-ui",
    ),
]
graphql = [path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True)))]

urlpatterns = admin + auth + docs + graphql
