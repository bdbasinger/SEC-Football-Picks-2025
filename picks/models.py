from django.db import models
from django.conf import settings
from games.models import Game

class Pick(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='picks'
    )
    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        related_name='picks'
    )
    picked_winner = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user} -> {self.picked_winner} for {self.game}"
