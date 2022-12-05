import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from django.conf import settings


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
    print(playlists)
    return playlists
    
    # for item in playlist1:
    

