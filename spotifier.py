"""Module that handles Spotify interactions"""

import configparser
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials

def auth(username, source="cmd"): # I WILL USE THIS ARGUMENT IN THE FUTURE FOR NOT HAVING TO PASTE REDIRECT URI ON CMD
    """Authenticates a user based in its username and uses a config.cfg file containing the client ID, client secret and redirection URI

    Args:
        username (string): The user's name (or code if registered with Facebook)
        source (string, optional): Where is the code being called from. Possible values are 'cmd' and 'gui'
    """
    print("Authing user...")
    scope = "user-library-read"

    config = configparser.ConfigParser()
    config.read('credentials.cfg')
    client_id = config.get('SPOTIFY', 'CLIENT_ID')
    client_secret = config.get('SPOTIFY', 'CLIENT_SECRET')
    redirect_uri = config.get('SPOTIFY', 'REDIRECT_URI')

    global sp
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, username=username))
    print("User authenticated succesfully!")

def get_saved_tracks():
    """Gets a list of dictionaries containing the loved songs on Spotify and returns it

    Returns:
        list: List of dictionaries containing all the information needed.
    """
    print("We'll get your favorite songs' list.")
    results = sp.current_user_saved_tracks()
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    print("We got the list!")
    return tracks