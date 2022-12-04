from django.shortcuts import render
from django.views.generic import TemplateView, View
from main import api

class HomepageView(TemplateView):
    template_name = 'homebase/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class VolumesView(TemplateView):
    template_name = 'volumes/volumes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class VolumeView(TemplateView):
    template_name = 'volumes/volume.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['volume'] = 'img/volumes/volume'+str(kwargs['volumenum'])+'.png'
        context['volumenum'] = kwargs['volumenum']
        return context

class MusicShelvesView(TemplateView):
    template_name = 'music/shelves.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # api.get_user_playlist()
        context['my_playlist'] = api.get_user_playlist()
        return context
