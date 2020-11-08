from django.db import models

from common.mixins import CreateModifyDateMixin

from kakkop.models.player import Player
from kakkop.models.round import Round


class RoundDetail(CreateModifyDateMixin):
    round = models.ForeignKey(
        Round, on_delete=models.CASCADE, related_name="round_details"
    )
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    bid = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
    cumulative_score = models.IntegerField(default=0)
