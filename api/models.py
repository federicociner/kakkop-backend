from django.db import models

from users.models import CustomUser


class Game(models.Model):
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    number_of_rounds = models.IntegerField(default=0)
    number_of_players = models.IntegerField(default=0)
    status = models.CharField(max_length=16, default="setup")
    game_type = models.CharField(max_length=32)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "games"
