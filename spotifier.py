"""Module that handles Spotify interactions"""

import configparser
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials

def auth(username):
    scope = "user-library-read"

    config = configparser.ConfigParser()
    config.read('config.cfg')
    client_id = config.get('SPOTIFY', 'CLIENT_ID')
    client_secret = config.get('SPOTIFY', 'CLIENT_SECRET')
    redirect_uri = config.get('SPOTIFY', 'REDIRECT_URI')

    global sp
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, username=username))

def get_saved_tracks():
    results = sp.current_user_saved_tracks()
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks