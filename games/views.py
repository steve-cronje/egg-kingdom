from django.shortcuts import render
from django.views.generic import TemplateView
from games.models import Game

class GamesShelvesView(TemplateView):
    template_name = 'games/shelves.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_games'] = Game.objects.all()
        return context
