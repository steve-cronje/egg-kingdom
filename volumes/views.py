from django.shortcuts import render
from django.views.generic import TemplateView

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