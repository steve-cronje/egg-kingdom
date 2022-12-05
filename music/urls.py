from django.urls import path
from music.views import MusicShelfView, MusicShelvesView

urlpatterns = [
    path('shelves/playlist/<str:id>', MusicShelfView.as_view(), name='playlist'),
    path('shelves/', MusicShelvesView.as_view(), name='music-shelves'),
]