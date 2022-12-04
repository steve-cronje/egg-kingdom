from django.shortcuts import render
from django.views.generic import TemplateView
from music import api

# Create your views here.

class MusicShelvesView(TemplateView):
    template_name = 'music/shelves.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # api.get_user_playlist()
        context['playlists'] = api.get_user_playlists_details()
        # print(api.get_user_playlist1())
        return context

class MusicShelfView(TemplateView):
    template_name = 'music/shelf.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # api.get_user_playlist()
        context['my_playlist'] = api.get_user_playlist_tracks(kwargs['playlist'])
        # print(api.get_user_playlist1())
        return context