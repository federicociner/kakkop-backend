from rest_framework import serializers
from api.models import Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "creator",
            "num_rounds",
            "num_players",
            "status",
            "game_type",
        )
        model = Game
