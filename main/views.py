from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from main.models import Ovum

class HomepageView(TemplateView):
    template_name = 'homebase/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class OvumDetailView(DetailView):

    template_name = 'homebase/ovum.html'
    model = Ovum