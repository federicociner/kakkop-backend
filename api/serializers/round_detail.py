from rest_framework.serializers import ModelSerializer

from ..models.round_detail import RoundDetail


class RoundDetailSerializer(ModelSerializer):
    class Meta:
        model = RoundDetail
        fields = [
            "id",
            "round",
            "player",
            "bid",
            "score",
            "cumulative_score",
        ]
