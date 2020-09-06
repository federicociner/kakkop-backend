from django.db import models

from common.models import BaseModel
from users.models import BaseUser

from .game import Game


class Player(BaseModel):
    user = models.ForeignKey(BaseUser, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    is_first_dealer = models.BooleanField()
    position = models.IntegerField()

    class Meta:
        db_table = "players"
