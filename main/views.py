from django.shortcuts import render
from django.views.generic import TemplateView
from music.api import get_user_playlists_details

class HomepageView(TemplateView):
    template_name = 'homebase/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        get_user_playlists_details()
        return context
