from django.db import models

from common.mixins import CreateModifyDateMixin
from users.models import BaseUser as User


class Game(CreateModifyDateMixin):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="games")
    status = models.CharField(
        choices=[("in_progress", "In progress"), ("completed", "Completed")],
        default="in_progress",
        max_length=16,
    )
    game_type = models.CharField(
        choices=[("hannibal", "Hannibal"), ("uno", "Uno")], max_length=32
    )
    number_of_rounds = models.IntegerField(default=0)
