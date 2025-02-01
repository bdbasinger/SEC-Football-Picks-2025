# picks/forms.py
from django import forms
from django.forms import modelformset_factory
from .models import Pick

class PickForm(forms.ModelForm):
    class Meta:
        model = Pick
        fields = ['outcome']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.instance.pk:
            # This is a brand-new (not from DB) pick
            # If you aren't setting game anywhere, you might skip or handle differently
            return
        if self.instance.game_id:
            # The normal logic
            game = self.instance.game
            self.fields['outcome'].choices = [
                ('HOME', game.home_team),
                ('AWAY', game.away_team),
            ]



PickFormSet = modelformset_factory(
    Pick,
    form=PickForm,
    extra=0,
    can_delete=False
)
