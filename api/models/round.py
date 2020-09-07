from django.db import models

from common.models import BaseModel

from .game import Game
from .player import Player


class Round(BaseModel):
    game = models.ForeignKey(
        Game, on_delete=models.CASCADE, related_name="rounds"
    )
    dealer = models.ForeignKey(Player, on_delete=models.CASCADE)
    status = models.CharField(
        choices=[
            ("notStarted", "Not started"),
            ("inProgress", "In progress"),
            ("completed", "Completed"),
        ],
        default="notStarted",
        max_length=16,
    )
    number_of_cards = models.IntegerField(default=0)

    class Meta:
        db_table = "rounds"
