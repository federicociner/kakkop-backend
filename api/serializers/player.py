from rest_framework.serializers import ModelSerializer

from ..models.player import Player


class PlayerSerializer(ModelSerializer):
    class Meta:
        model = Player
        fields = (
            "id",
            "user",
            "game",
            "is_first_dealer",
            "position",
        )
