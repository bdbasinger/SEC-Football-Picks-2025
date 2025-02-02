# picks/forms.py
from django import forms
from django.forms import modelformset_factory
from .models import Pick, Game

class PickForm(forms.ModelForm):
    class Meta:
        model = Pick
        fields = ['id','outcome']
        widgets = {'id': forms.HiddenInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.game_id:  # Ensure game exists
            game = self.instance.game
            self.fields['outcome'].choices = [
                ('HOME', game.home_team),  # Shows home team name
                ('AWAY', game.away_team),  # Shows away team name
            ]
        print("Form instance ID:", self.instance.pk)  # Debugging line


PickFormSet = modelformset_factory(
    Pick,
    form=PickForm,
    extra=0,
    can_delete=False
)
