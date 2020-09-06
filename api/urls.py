from django.urls import include, path

from .views.game import GameDetailApi, GameListApi
from .views.player import PlayerDetailApi, PlayerListApi

game_patterns = [
    path("", GameListApi.as_view(), name="game_list"),
    path("<int:pk>/", GameDetailApi.as_view(), name="game_detail"),
]

player_patterns = [
    path("", PlayerListApi.as_view(), name="player_list"),
    path("<int:pk>/", PlayerDetailApi.as_view(), name="player_detail"),
]

urlpatterns = [
    path("games/", include((game_patterns, "games"))),
    path("players/", include((player_patterns, "players"))),
]
