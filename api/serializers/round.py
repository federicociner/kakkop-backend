from rest_framework.serializers import ModelSerializer

from ..models.round import Round


class RoundSerializer(ModelSerializer):
    class Meta:
        model = Round
        fields = ["id", "game", "dealer", "status", "number_of_cards"]
        read_only_fields = ["game", "dealer"]
