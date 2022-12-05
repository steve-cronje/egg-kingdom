import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from django.conf import settings
from music.models import Track, Album, Artist
import re

def pmwp(playlist_id):
    auth_manager = SpotifyClientCredentials(client_id=settings.SPOTIFY_CLIENT_ID, client_secret=settings.SPOTIFY_CLIENT_SECRET)
    sp = spotipy.Spotify(auth_manager=auth_manager)
    playlist = sp.user_playlist('mrpotato252', playlist_id)
    for item in playlist['tracks']['items']:
        artists = item['track']['artists']
        for x in artists:
            artist, artist_created = Artist.objects.get_or_create(id=x['id'])
            if artist_created:
                artist.name = x['name']
                artist.artist_type = x['type']
                artist.spotify_url = x['external_urls']['spotify']
                artist.save()
        for x in item['track']['album']['artists']:
            artist, artist_created = Artist.objects.get_or_create(id=x['id'])
            if artist_created:
                artist.name = x['name']
                artist.artist_type = x['type']
                artist.spotify_url = x['external_urls']['spotify']
                artist.save()
    
    print('\n------- all artists saved! -------')

    for item in playlist['tracks']['items']:
        album, album_created = Album.objects.get_or_create(id=item['track']['album']['id'])
        if album_created:
            album.name = item['track']['album']['name']
            album.album_type = item['track']['album']['album_type']
            for artist in item['track']['album']['artists']:
                album.artists.add(artist['id'])
            album.image_url = item['track']['album']['images'][1]['url']
            album.image_url_big = item['track']['album']['images'][0]['url']
            album.spotify_url = item['track']['album']['external_urls']['spotify']
            album.release_date = item['track']['album']['release_date'] if re.compile('\d\d\d\d-\d\d-\d\d').match(item['track']['album']['release_date']) else item['track']['album']['release_date']+'-01-01'
            album.save()


        track, track_created = Track.objects.get_or_create(id=item['track']['id'])
        if track_created:
            track.name = item['track']['name']
            track.album = album
            for artist in item['track']['artists']:
                track.artists.add(artist['id'])
            track.preview_url = item['track']['preview_url']
            track.spotify_url = item['track']['external_urls']['spotify']
            track.explicit_content = True if item['track']['explicit'] == 'True' else False
            track.duration = item['track']['duration_ms']
            track.save()

    print('\n------- all tracks & albums saved! -------')


def ue(playlist_id):
    auth_manager = SpotifyClientCredentials(client_id=settings.SPOTIFY_CLIENT_ID, client_secret=settings.SPOTIFY_CLIENT_SECRET)
    sp = spotipy.Spotify(auth_manager=auth_manager)
    playlist = sp.user_playlist('mrpotato252', playlist_id)
    for item in playlist['tracks']['items']:
        Track.objects.get(id=item['track']['id']).explicit_content = bool(item['track']['explicit'])
        print('explicit content boolean changed!')