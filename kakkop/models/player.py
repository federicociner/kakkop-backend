from django.db import models

from common.models import BaseModel
from users.models import BaseUser

from .game import Game


class Player(BaseModel):
    user = models.ForeignKey(BaseUser, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="players")
    position = models.IntegerField()
    is_first_dealer = models.BooleanField()
