from django.db import models

class Game(models.Model):
    date = models.DateField()
    home_team = models.CharField(max_length=100)
    away_team = models.CharField(max_length=100)
    home_score = models.IntegerField(null=True, blank=True)
    away_score = models.IntegerField(null=True, blank=True)

    def winner(self):
        """
        Returns the string name of the winning team if scores are present.
        Otherwise returns None.
        """
        if self.home_score is not None and self.away_score is not None:
            if self.home_score > self.away_score:
                return self.home_team
            elif self.away_score > self.home_score:
                return self.away_team
        return None

    def __str__(self):
        # A quick representation for the admin or shell
        return f"{self.away_team} at {self.home_team} on {self.date}"
