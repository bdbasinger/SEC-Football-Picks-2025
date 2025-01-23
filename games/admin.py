from django.contrib import admin
from .models import Game

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('date', 'home_team', 'away_team')
