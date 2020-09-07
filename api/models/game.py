from django.db import models

from common.models import BaseModel
from users.models import BaseUser


class Game(BaseModel):
    creator = models.ForeignKey(BaseUser, on_delete=models.CASCADE)
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
