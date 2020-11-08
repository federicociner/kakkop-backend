from django.db import models

from common.mixins import CreateModifyDateMixin
from users.models import BaseUser as User

from kakkop.models.game import Game


class Player(CreateModifyDateMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="players")
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="players")
    position = models.IntegerField()
    is_first_dealer = models.BooleanField()
