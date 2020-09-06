from rest_framework.serializers import ModelSerializer

from ..models.game import Game


class GameSerializer(ModelSerializer):
    class Meta:
        model = Game
        fields = (
            "id",
            "creator",
            "number_of_rounds",
            "number_of_players",
            "status",
            "game_type",
        )
