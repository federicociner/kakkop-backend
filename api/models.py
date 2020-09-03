from django.db import models

from common.models import BaseModel
from users.models import BaseUser


class Game(BaseModel):
    creator = models.ForeignKey(BaseUser, on_delete=models.CASCADE)
    number_of_rounds = models.IntegerField(default=0)
    number_of_players = models.IntegerField()
    status = models.CharField(
        choices=[
            ("setup", "Setup"),
            ("inProgress", "In progress"),
            ("completed", "Completed"),
        ],
        default="setup",
        max_length=16,
    )
    game_type = models.CharField(
        choices=[("hannibal", "Hannibal"), ("uno", "Uno")], max_length=32
    )

    class Meta:
        db_table = "games"


class Player(BaseModel):
    user = models.ForeignKey(BaseUser, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    is_first_dealer = models.BooleanField()
    position = models.IntegerField()

    class Meta:
        db_table = "players"
