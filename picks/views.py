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


from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from itertools import groupby
from operator import attrgetter
from .models import Pick
from games.models import Game
from .forms import PickFormSet


@login_required
def make_all_picks(request):
    all_games = Game.objects.all()
    existing_picks = Pick.objects.filter(user=request.user).select_related('game')
    existing_game_ids = {p.game_id for p in existing_picks}

    new_picks = [
        Pick(user=request.user, game=game)
        for game in all_games
        if game.id not in existing_game_ids
    ]
    Pick.objects.bulk_create(new_picks)

    queryset = Pick.objects.filter(user=request.user, id__isnull=False).select_related('game')


    if request.method == 'POST':
        formset = PickFormSet(request.POST, queryset=queryset)

        # **DEBUGGING LINES**:
        print("POST DATA:", request.POST)  # Look at the raw POST data
        if formset.is_valid():
            # If valid, show which data was cleaned
            for i, form in enumerate(formset):
                print(f"Form {i} cleaned_data:", form.cleaned_data)
            formset.save()
            return redirect('picks_success')
        else:
            # If invalid, display errors for each form
            for i, form in enumerate(formset):
                print(f"Form {i} errors:", form.errors)
            # You might fall through to re-render the formset below
            # so the user can correct errors.
    else:
        formset = PickFormSet(queryset=queryset)

    forms_by_week = {}
    for form in formset:
        w = form.instance.game.week
        # If the dictionary doesn't have this week yet, create an empty list
        forms_by_week.setdefault(w, []).append(form)




    return render(request, 'picks/make_all_picks.html', {
        'formset': formset,
        'forms_by_week': forms_by_week
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




