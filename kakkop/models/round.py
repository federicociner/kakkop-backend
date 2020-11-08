from django.db import models

from common.mixins import CreateModifyDateMixin

from kakkop.models.game import Game
from kakkop.models.player import Player


class Round(CreateModifyDateMixin):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="rounds")
    dealer = models.ForeignKey(Player, on_delete=models.CASCADE)
    number = models.IntegerField()
    status = models.CharField(
        choices=[
            ("not_started", "Not started"),
            ("in_progress", "In progress"),
            ("completed", "Completed"),
        ],
        default="not_started",
        max_length=16,
    )
    number_of_cards = models.IntegerField(default=0)
