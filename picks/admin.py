from django.contrib import admin
from .models import Pick

@admin.register(Pick)
class PickAdmin(admin.ModelAdmin):
    list_display = ('user', 'game', 'picked_winner')
