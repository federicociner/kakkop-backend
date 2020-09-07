from rest_framework.serializers import ModelSerializer

from ..models.game import Game
from ..models.player import Player
from ..models.round import Round
from .player import PlayerSerializer
from .round import RoundSerializer


class GameSerializer(ModelSerializer):
    players = PlayerSerializer(many=True)
    rounds = RoundSerializer(many=True, read_only=True)

    class Meta:
        model = Game
        fields = [
            "id",
            "creator",
            "status",
            "game_type",
            "players",
            "rounds",
        ]

    def create(self, validated_data):
        players_data = validated_data.pop("players")
        game = Game.objects.create(**validated_data)

        # Generate players
        for data in players_data:
            dealer = Player.objects.create(game=game, **data)

        # Generate rounds
        for i in range(10):
            Round.objects.create(game=game, dealer=dealer)

        return game
