# picks/urls.py
from django.urls import path
from .views import picks_home, create_pick_view, leaderboard_view, make_all_picks
from . import views

urlpatterns = [
    path('', picks_home, name='picks_home'),
    path('create/<int:game_id>/', create_pick_view, name='create_pick'),
    path('leaderboard/', leaderboard_view, name='leaderboard'),
    path('make_all_picks/', views.make_all_picks, name='make_all_picks'),
    path('success/', views.picks_success, name='picks_success'),

]
