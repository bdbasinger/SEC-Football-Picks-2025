# picks/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Pick
from games.models import Game
from django.contrib.auth import get_user_model




from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from games.models import Game
from .models import Pick
from .forms import PickFormSet

@login_required
def make_all_picks(request):
    # 1. Get all games (you can filter by date or status if needed)
    all_games = Game.objects.all()

    # 2. Check existing picks for this user (CustomUser)
    existing_picks = Pick.objects.filter(user=request.user).select_related('game')
    existing_game_ids = {p.game_id for p in existing_picks}

    # 3. Create new picks in bulk for any games missing a pick
    new_picks = [
        Pick(user=request.user, game=game) #.id
        for game in all_games
        if game.id not in existing_game_ids
    ]
    Pick.objects.bulk_create(new_picks)  # This creates rows in the DB if they don't exist

    # Now every game has a pick for this user
    queryset = Pick.objects.filter(user=request.user).select_related('game')

    if request.method == 'POST':
        formset = PickFormSet(request.POST, queryset=queryset)
        if formset.is_valid():
            formset.save()  # Saves all updated picks at once
            return redirect('picks_success')  # Or wherever you want
    else:
        formset = PickFormSet(queryset=queryset)

    return render(request, 'picks/make_all_picks.html', {
        'formset': formset,
    })



# picks/views.py
def picks_success(request):
    return render(request, 'picks/picks_success.html')



def leaderboard_view(request):
    User = get_user_model()
    users = User.objects.all()
    scoreboard = []

    for user in users:
        user_picks = Pick.objects.filter(user=user)
        correct_count = 0
        for pick in user_picks:
            if pick.game.winner() == pick.outcome:
                correct_count += 1
        scoreboard.append((user, correct_count))

    # Sort by correct picks descending
    scoreboard.sort(key=lambda x: x[1], reverse=True)

    return render(request, 'picks/leaderboard.html', {'scoreboard': scoreboard})



@login_required
def picks_home(request):
    # Show all picks for this user, or provide links/forms to create them.

    user_picks = Pick.objects.filter(user=request.user)
    return render(request, 'picks/picks_home.html', {'user_picks': user_picks})



@login_required
def create_pick_view(request, game_id):
    # Create or update a user's pick for a specific game.

    game = get_object_or_404(Game, pk=game_id)

    if request.method == 'POST':
        picked_winner = request.POST.get('outcome')
        # If the user already picked this game, update; otherwise create
        pick, created = Pick.objects.update_or_create(
            user=request.user,
            game=game,
            defaults={'outcome': picked_winner}
        )
        return redirect('picks_home')

    # If GET, we show a simple form to pick the winner
    return render(request, 'picks/create_pick.html', {'game': game})




