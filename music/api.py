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

    playlist = []
    for item in playlists['tracks']['items']:
        name = item['track']['name']
        image = item['track']['album']['images'][1]['url']
        artists = item['track']['artists']
        artist_names = ''
        if len(artists) > 1:
            artist_names = ''
            for x in artists:
                artist_names += x['name']+', '
            artist_names = artist_names[:(len(artist_names)-2):]
        else:
            artist_names = artists[0]['name']
        album = ''
        if item['track']['album']['album_type'] == 'single':
            album = 'Single'
        else:
            album = item['track']['album']['name']
        preview_url = item['track']['preview_url']
        track_url = item['track']['external_urls']['spotify']

        
        playlist.append({'name': name, 'image': image, 'artists': artist_names, 'album': album, 'preview_url': preview_url, 'track_url': track_url})
    # print(playlist)
    return playlist

