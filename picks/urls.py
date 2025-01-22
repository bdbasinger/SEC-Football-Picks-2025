# picks/urls.py
from django.urls import path
from .views import picks_view

urlpatterns = [
    path('', picks_view, name='picks'),
]
