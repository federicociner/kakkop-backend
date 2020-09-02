from rest_framework import generics

from api.models import Game
from api.serializers import GameSerializer


class GameList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
