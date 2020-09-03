from rest_framework import serializers

from api.models import Game


class GameSerializer(serializers.ModelSerializer):
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
