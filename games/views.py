from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView, FormView, UpdateView, CreateView, DeleteView
from games.models import Game
import games.api as api
from games.forms import GameAddForm, GameEditForm

class GamesView(ListView):
    template_name = 'games/games.html'
    model = Game

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_games'] = self.model.objects.all().order_by('release_date')
        context['favourites'] = self.model.objects.filter(favourite=True).order_by('release_date')
        context['abs_favourites'] = self.model.objects.filter(abs_favourite=True).order_by('release_date')
        context['want'] = self.model.objects.filter(want=True).order_by('release_date')
        return context

class GameDisplayView(DetailView):
    template_name = 'games/game.html'
    model = Game


class GameAddView(CreateView):

    template_name = "games/addform.html"
    model = Game
    form_class = GameAddForm
    
    def post(self, request, *args, **kwargs):
        game = api.add_game_with_id(int(request.POST['game_id']), request.POST['my_description'])
        return redirect(game)

class GameEditView(UpdateView):

    template_name = "games/editform.html"
    form_class = GameEditForm
    model = Game    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['game_id'] = self.get_object().id
        return context


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


def game_favourite_update_view(request, pk):

    game = get_object_or_404(Game, pk=pk)
    game.make_favourite(int(request.POST['favourite']))
    return redirect(game)


class GameDeleteView(DeleteView):

    model = Game
    success_url = "/games/shelves/"
    template_name = "games/deleteform.html"
    context_object_name = 'game'

    