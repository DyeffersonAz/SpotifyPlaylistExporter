"""Module that handles Spotify interactions"""

import configparser
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials

def auth(username):
    """Authenticates a user based in its username and uses a config.cfg file containing the client ID, client secret and redirection URI

    Args:
        username (string): The user's name (or code if registered with Facebook)
    """
    print("Autenticando Usuário...")
    scope = "user-library-read"

    config = configparser.ConfigParser()
    config.read('config.cfg')
    client_id = config.get('SPOTIFY', 'CLIENT_ID')
    client_secret = config.get('SPOTIFY', 'CLIENT_SECRET')
    redirect_uri = config.get('SPOTIFY', 'REDIRECT_URI')

    global sp
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, username=username))
    print("Usuário autenticado com sucesso!")

def get_saved_tracks():
    """Gets a list of dictionaries containing the loved songs on Spotify and returns it

    Returns:
        list: List of dictionaries containing all the information needed.
    """
    print("Vamos pegar a lista das suas favoritas...")
    results = sp.current_user_saved_tracks()
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    print("Conseguimos a tal lista!")
    return tracks