from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
from django.forms import ModelForm
from datetime import date

from game.models import Game


class AddGameForm(ModelForm):
    game_date = forms.CharField(widget=forms.TextInput(attrs={'type': 'date'}),
                           validators=[MinValueValidator(limit_value=date.today().strftime('%Y-%m-%d'),
                                                         message="Past Date")])

    class Meta:
        model = Game
        fields = ['stadium', 'price', 'max_players', 'game_date','status']
