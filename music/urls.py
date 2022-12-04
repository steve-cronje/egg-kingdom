from django.urls import path
from music.views import MusicShelfView, MusicShelvesView

urlpatterns = [
    path('shelves', MusicShelvesView.as_view(), name='music-shelves'),
    path('shelves/<str:playlist>', MusicShelfView.as_view(), name='playlist'),
]