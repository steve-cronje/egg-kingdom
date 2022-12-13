from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from games.models import Game
import games.api as api

class GamesShelvesView(ListView):
    template_name = 'games/shelves.html'
    model = Game

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_games'] = self.model.objects.all().order_by('release_date')
        return context

class GameDisplayView(DetailView):
    template_name = 'games/game.html'
    model = Game

class CallApiView(TemplateView):
    template_name = 'games/api.html'
    model = Game

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # csv_list = api.parse_gameslist_csv('C:\\Users\\Potato\\Desktop\\index-ludorum-pro-ovo-rege.csv')
        # api.populate_gamesdb_with_data('C:\\Users\\Potato\\Desktop\\json_gameslist.txt')
        # api.get_igdb_data_from_db()
        # print(csv_list)
        return context
