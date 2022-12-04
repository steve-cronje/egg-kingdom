from django.urls import path
from music.views import MusicShelvesView

urlpatterns = [
    path('shelves/', MusicShelvesView.as_view(), name='music-shelves'),
]