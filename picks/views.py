# picks/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Pick
from games.models import Game

@login_required
def picks_home(request):
    """
    Show all picks for this user, or provide links/forms to create them.
    """
    user_picks = Pick.objects.filter(user=request.user)
    return render(request, 'picks/picks_home.html', {'user_picks': user_picks})

@login_required
def create_pick_view(request, game_id):
    """
    Create or update a user's pick for a specific game.
    """
    game = get_object_or_404(Game, pk=game_id)

    if request.method == 'POST':
        picked_winner = request.POST.get('picked_winner')
        # If the user already picked this game, update; otherwise create
        pick, created = Pick.objects.update_or_create(
            user=request.user,
            game=game,
            defaults={'picked_winner': picked_winner}
        )
        return redirect('picks_home')

    # If GET, we show a simple form to pick the winner
    return render(request, 'picks/create_pick.html', {'game': game})
