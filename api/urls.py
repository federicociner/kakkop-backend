from django.urls import include, path

from .views import GameApi, GameDetailApi

game_patterns = [
    path("", GameApi.as_view(), name="list"),
    path("<int:pk>/", GameDetailApi.as_view(), name="detail"),
]

urlpatterns = [path("games/", include((game_patterns, "games")))]
