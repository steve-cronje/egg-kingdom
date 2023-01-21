from django.shortcuts import render
from django.views.generic import ListView, DetailView
from volumes.models import Meme

class VolumesView(ListView):

    template_name = 'volumes/volumes.html'
    model = Meme
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['memes'] = Meme.objects.all()
        return context

class VolumeView(DetailView):

    template_name = 'volumes/volume.html'
    model = Meme