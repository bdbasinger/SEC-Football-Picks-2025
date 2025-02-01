

# picks/models.py
from django.conf import settings
from django.db import models
from games.models import Game  # or however you're importing your Game model

class Pick(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # references the custom user model
        on_delete=models.CASCADE
    )
    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        related_name='picks')

    OUTCOME_CHOICES = [
        ('HOME', 'Home Team'),
        ('AWAY', 'Away Team'),
    ]
    outcome = models.CharField(max_length=10, choices=OUTCOME_CHOICES)

    class Meta:
        unique_together = ('user', 'game')

    def __str__(self):
        return f"{self.user.email} - {self.game} - {self.outcome}"

    def picked_winner(self):
        """Returns the team name based on the outcome."""
        if self.outcome == 'HOME':
            return self.game.home_team
        elif self.outcome == 'AWAY':
            return self.game.away_team
        return "No winner selected"

    # Make it more readable in the admin
    picked_winner.short_description = "Picked Winner"
