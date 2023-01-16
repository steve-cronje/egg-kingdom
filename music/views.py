from django.shortcuts import render
from django.views.generic import TemplateView
from music.models import Playlist
from music.api import populate_database_data, remove_unused
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
            context['my_playlist'] = playlist
        return context


class UpdatePlaylistsView(TemplateView):
    template_name = 'music/updateplaylist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['playlist_id'] = kwargs['id']
        context['returned_list'] = populate_database_data(kwargs['id'])
        # context['removed_list'] = remove_unused(kwargs['id'])
        return context