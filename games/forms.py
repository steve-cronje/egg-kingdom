from django import forms
from games.models import Game

class GameAddForm(forms.Form):
    game_id = forms.IntegerField()
    my_description = forms.CharField()

    game_id.widget.attrs.update({'class': 'form-control game-id', 'placeholder': 0000})
    my_description.widget.attrs.update({'class': 'form-control game-text', 'placeholder': 'My Description'})

class GameEditForm(forms.ModelForm):
    name = forms.CharField()
    my_description = forms.CharField()
    class Meta:
        
        model = Game
        fields = ['name', 'my_description']

    name.widget.attrs.update({'class': 'form-control game-id', 'placeholder': "name"})
    my_description.widget.attrs.update({'class': 'form-control game-text', 'placeholder': 'My Description'})