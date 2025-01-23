# picks/urls.py
from django.urls import path
from .views import picks_home, create_pick_view, leaderboard_view

urlpatterns = [
    path('', picks_home, name='picks_home'),
    path('create/<int:game_id>/', create_pick_view, name='create_pick'),
    path('leaderboard/', leaderboard_view, name='leaderboard'),
]
