from django.shortcuts import render
from django.views.generic import TemplateView
from music.models import Playlist

class MusicShelvesView(TemplateView):
    template_name = 'music/shelves.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['playlists'] = Playlist.objects.all()
        return context

class MusicShelfView(TemplateView):
    template_name = 'music/playlist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if kwargs['id'] != 'None':
            playlist = Playlist.objects.get(id=kwargs['id'])
            context['playlist_url'] = playlist.spotify_url
            context['my_playlist'] = playlist.track_set.all()
        return context