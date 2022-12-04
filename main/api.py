import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from django.conf import settings
from django.urls import reverse


def print_spotipy():  
    auth_manager = SpotifyClientCredentials(client_id=settings.SPOTIFY_CLIENT_ID, client_secret=settings.SPOTIFY_CLIENT_SECRET)
    sp = spotipy.Spotify(auth_manager=auth_manager)

    playlists = sp.user('mrpotato252')
    print(playlists)

def get_user_playlist():
    auth_manager = SpotifyClientCredentials(client_id=settings.SPOTIFY_CLIENT_ID, client_secret=settings.SPOTIFY_CLIENT_SECRET)
    sp = spotipy.Spotify(auth_manager=auth_manager)

    # user = sp.user('mrpotato252')
    playlists = sp.user_playlist('mrpotato252', '3382J1fcy8RhhyA9LOoy84?si=a49c6dc16e6d4bb5')

    playlist = [(x['track']['name'], x['track']['album']['images'][1]['url']) for x in playlists['tracks']['items']]
    # print(playlists['tracks'])
    return playlist

