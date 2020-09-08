from rest_framework.serializers import ModelSerializer

from .. import constants
from ..models.game import Game
from ..services.hannibal import HannibalGameService
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
            "number_of_rounds",
            "players",
            "rounds",
        ]

    def create(self, validated_data):
        players_data = validated_data.pop("players")
        game = Game.objects.create(**validated_data)
        service = None

        if validated_data["game_type"] == constants.HANNIBAL:
            service = HannibalGameService()

        service.generate_players(game, players_data)
        service.generate_rounds(game)

        return game
