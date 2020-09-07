from django.db import models

from common.models import BaseModel

from .player import Player
from .round import Round


class RoundDetail(BaseModel):
    round = models.ForeignKey(
        Round, on_delete=models.CASCADE, related_name="round_details"
    )
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    bid = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
    cumulative_score = models.IntegerField(default=0)

    class Meta:
        db_table = "round_details"
