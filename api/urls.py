from django.urls import path

from api.views import GameList

urlpatterns = [
    path("games", GameList.as_view()),
]
