import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from django.conf import settings
from music.models import Track, Album, Artist
import re


def get_user_playlist_tracks(playlist_id):
    auth_manager = SpotifyClientCredentials(client_id=settings.SPOTIFY_CLIENT_ID, client_secret=settings.SPOTIFY_CLIENT_SECRET)
    sp = spotipy.Spotify(auth_manager=auth_manager)

    playlists = sp.user_playlist('mrpotato252', playlist_id)

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
    playlist_name = playlists['name']
    playlist_url = playlists['external_urls']['spotify']
    return [playlist, playlist_name, playlist_url]

def get_user_playlists_details():
    auth_manager = SpotifyClientCredentials(client_id=settings.SPOTIFY_CLIENT_ID, client_secret=settings.SPOTIFY_CLIENT_SECRET)
    sp = spotipy.Spotify(auth_manager=auth_manager)

    playlists = []
    for playlist_id in ['3382J1fcy8RhhyA9LOoy84', '2LUCK2ZsBfddsCabOqU9D9']:
        playlist = sp.user_playlist('mrpotato252', playlist_id)
        playlist_image = playlist['images'][0]['url']
        playlist_name = playlist['name']
        playlist_url = playlist['external_urls']
        playlists.append({'name': playlist_name, 'image': playlist_image, 'id': playlist_id, 'url': playlist_url['spotify']})
    # print(playlists)
    return playlists


def populate_database_data(playlist_id):
    auth_manager = SpotifyClientCredentials(client_id=settings.SPOTIFY_CLIENT_ID, client_secret=settings.SPOTIFY_CLIENT_SECRET)
    sp = spotipy.Spotify(auth_manager=auth_manager)
    playlist = sp.user_playlist('mrpotato252', playlist_id)
    list_of_errors = []
    list_of_new_objects = []
    for item in playlist['tracks']['items']:
        try:
            artists = item['track']['artists']
            for x in artists:
                artist, artist_created = Artist.objects.get_or_create(id=x['id'])
                if artist_created:
                    artist.name = x['name']
                    artist.artist_type = x['type']
                    artist.spotify_url = x['external_urls']['spotify']
                    artist.save()
                    list_of_new_objects.append((artist.name, 'Artist'))

            for x in item['track']['album']['artists']:
                artist, artist_created = Artist.objects.get_or_create(id=x['id'])
                if artist_created:
                    artist.name = x['name']
                    artist.artist_type = x['type']
                    artist.spotify_url = x['external_urls']['spotify']
                    artist.save()
                    list_of_new_objects.append((artist.name, 'Artist'))


        except Exception as e:
            list_of_errors.append((e, item))
    for item in playlist['tracks']['items']:
        try:
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
                list_of_new_objects.append((album.name, 'Album'))


            track, track_created = Track.objects.get_or_create(id=item['track']['id'])
            if track_created:
                track.name = item['track']['name']
                track.album = album
                for artist in item['track']['artists']:
                    track.artists.add(artist['id'])
                track.playlist.add(playlist_id)
                track.preview_url = item['track']['preview_url']
                track.spotify_url = item['track']['external_urls']['spotify']
                track.explicit_content = item['track']['explicit']
                track.duration = item['track']['duration_ms']
                track.save()
                list_of_new_objects.append((track.name, 'Track'))
        except Exception as e:
            list_of_errors.append((e, item))

    return (False, list_of_errors) if len(list_of_errors) > 0 else (True, list_of_new_objects)

'''TODO create api method that removed tracks / albums / artists from database if not in spotify playlists'''

