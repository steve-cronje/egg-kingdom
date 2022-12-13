from django.urls import path
from music.views import MusicShelfView, MusicShelvesView, UpdatePlaylistsView

urlpatterns = [
    path('shelves/playlist/update/<str:id>', UpdatePlaylistsView.as_view(), name='update-playlist'),
    path('shelves/playlist/<str:id>', MusicShelfView.as_view(), name='playlist'),
    path('shelves/', MusicShelvesView.as_view(), name='music-shelves'),
]