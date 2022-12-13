from django.conf import settings
import pandas as pd
import igdb.wrapper as iwrap
import json
from games.models import Game, Company, Genre, Screenshot
from requests import HTTPError
import datetime


def parse_gameslist_csv(csv_url):
    games_csv = pd.read_csv(csv_url)
    my_list = []
    for item in games_csv.iterrows():
        x = item[1]
        my_list.append({'Name': x.game, 'id': x.id, 'genres': x.genres, 'companies': x.companies, 'description': x.description, 'release_date': x.release_date})
    return my_list


def populate_gamesdb_with_data(list_url):
    pass


def get_igdb_data_from_db():
    wrapper = iwrap.IGDBWrapper(settings.TWITCH_IGDB_CLIENT_ID, settings.TWITCH_IGDB_AUTH_TOKEN)
    game_count = Game.objects.count()
    for game in Game.objects.all():
        
            byte_array = wrapper.api_request('screenshots', f'fields url; where game={game.pk};')
            json_dump = json.loads(byte_array)
            # game.game_bio = storyline
            for screenshot in json_dump:
                image, created = Screenshot.objects.get_or_create(pk=screenshot['id'])
                image.url = screenshot['url'].replace('t_thumb', 't_cover_big')
                image.game = game
                image.save()
            game_count -= 1
            print(game_count, ' games left')

    print('\n\n\nall done!\n\n\n')


def populate_genre_and_company_data():
    pass


def get_twitch_auth_key():
    '''
    UNCOMMENT ME IF YOU NEED NEW TWITCH / IGDB AUTH TOKEN FOR API
    '''
    pass
    # client_id = settings.TWITCH_IGDB_CLIENT_ID
    # client_secret = settings.TWITCH_IGDB_CLIENT_SECRET
    # response = requests.post(url=f'https://id.twitch.tv/oauth2/token?client_id={client_id}&client_secret={client_secret}&grant_type=client_credentials')
    # print(response.json())