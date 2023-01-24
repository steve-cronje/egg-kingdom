from django.conf import settings
import pandas as pd
import igdb.wrapper as iwrap
import json
from games.models import Game, Company, Genre, Screenshot
import requests
from requests import HTTPError
import datetime



def get_screenshots(game: Game):
    wrapper = iwrap.IGDBWrapper(settings.TWITCH_IGDB_CLIENT_ID, settings.TWITCH_IGDB_AUTH_TOKEN)
    byte_array = wrapper.api_request('screenshots', f'fields url; where game={game.pk};')
    json_dump = json.loads(byte_array)
    for screenshot in json_dump:
        image, created = Screenshot.objects.get_or_create(pk=screenshot['id'])
        image.url = screenshot['url'].replace('t_thumb', 't_1080p')
        image.game = game
        image.save()
    print(f"Screenshots for {game.name} saved to database!")


def update_summaries():
    wrapper = iwrap.IGDBWrapper(settings.TWITCH_IGDB_CLIENT_ID, settings.TWITCH_IGDB_AUTH_TOKEN)
    for game in Game.objects.all():
        
        byte_array = wrapper.api_request('games', f'fields summary; where id={game.pk};')
        json_dump = json.loads(byte_array)[0]
        game.game_bio = json_dump['summary']
        game.save()
        print(f"summary for {game.name} saved!")
   


def get_twitch_auth_key():
    '''
    UNCOMMENT ME IF YOU NEED NEW TWITCH / IGDB AUTH TOKEN FOR API
    '''
    # pass
    # client_id = settings.TWITCH_IGDB_CLIENT_ID
    # client_secret = settings.TWITCH_IGDB_CLIENT_SECRET
    # response = requests.post(url=f'https://id.twitch.tv/oauth2/token?client_id={client_id}&client_secret={client_secret}&grant_type=client_credentials')
    # print(response.json())


def add_game_with_id(id, description):
    wrapper = iwrap.IGDBWrapper(settings.TWITCH_IGDB_CLIENT_ID, settings.TWITCH_IGDB_AUTH_TOKEN)
    byte_array = wrapper.api_request('games', f'fields name,first_release_date,summary,cover.url,genres.name; where id={id};')
    json_dump = json.loads(byte_array)[0]
    name = json_dump['name']
    rd = datetime.datetime.utcfromtimestamp(json_dump['first_release_date'])
    genres = [x['name'] for x in json_dump['genres']]
    storyline = json_dump['summary']
    cover = json_dump['cover']['url'].replace('t_thumb', 't_cover_big')

    game, created = Game.objects.get_or_create(id=id)
    game.name = name
    game.release_date = rd
    game.game_bio = storyline
    game.cover_url = cover
    for genre in genres:
        genre, genre_created = Genre.objects.get_or_create(genre=genre)
        game.genre.add(genre)
    game.my_description = description
    game.save()

    get_screenshots(game=game)

    return game


def update_game_genres(id):
    wrapper = iwrap.IGDBWrapper(settings.TWITCH_IGDB_CLIENT_ID, settings.TWITCH_IGDB_AUTH_TOKEN)
    byte_array = wrapper.api_request('games', f'fields genres.name; where id={id};')
    json_dump = json.loads(byte_array)[0]
    genres = [x['name'] for x in json_dump['genres']]
    game = Game.objects.get(id=id)
    for genre in genres:
        genre, genre_created = Genre.objects.get_or_create(genre=genre)
        game.genre.add(genre)
        print(f'added {genre} to {game}!')