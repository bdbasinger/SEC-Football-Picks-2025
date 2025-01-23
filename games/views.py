# games/views.py
from django.shortcuts import render, get_object_or_404
from .models import Game

def game_list_view(request):
    # Order by date so that earliest games appear first
    games = Game.objects.all().order_by('date')
    return render(request, 'games/game_list.html', {'games': games})

def game_detail_view(request, pk):
    game = get_object_or_404(Game, pk=pk)
    return render(request, 'games/game_detail.html', {'game': game})
