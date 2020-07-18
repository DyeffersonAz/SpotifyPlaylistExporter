"""Parses json spotify files into lists of tracks and lists of artists"""

import json

def parse(sjsonfile):
    """Gets a json string and makes it into a list of song's titles followed by the respective first artist on the song

    Args:
        sjsonfile (string): A string of a json file containing songs and all details provided by Spotify

    Returns:
        list: List of strings of songs followed by the first artist
    """
    jsonfile = json.loads(sjsonfile)
    songs = []
    for track in jsonfile:
        songs.append(f"{track['track']['name']} {track['track']['artists'][0]['name']}")
    return songs

def list_into_file(songs):
    """Makes a txt file from a list of song's titles followed by the respective first artist on the song

    Args:
        songs (list): List of songs, probably made by parse()
    """
    with open('songs.txt', 'w', encoding="UTF-8") as songsFile:
        for track in songs:
            songsFile.write(f"{track}\n")