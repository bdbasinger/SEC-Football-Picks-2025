# games/urls.py
from django.urls import path
from .views import game_list_view, game_detail_view

urlpatterns = [
    path('', game_list_view, name='game_list'),
    path('<int:pk>/', game_detail_view, name='game_detail'),
]
