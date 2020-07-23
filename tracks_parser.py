"""Parses json spotify files into lists of tracks and lists of artists"""

import json

def parse(sjsonfile):
    """Gets a json string and makes it into a list of song's titles followed by the respective first artist on the song

    Args:
        sjsonfile (string): A string of a json file containing songs and all details provided by Spotify

    Returns:
        list: List of lists of strings of songs as the first element followed by a string of the song's artists as the second element
    """
    jsonfile = json.loads(sjsonfile)
    songs = []
    for track in jsonfile:
        songs.append([track['track']['name'], artists(sjsonfile, jsonfile.index(track))])
    return songs

def list_into_file(songs):
    """Makes a txt file from a list of song's titles followed by the respective first artist on the song

    Args:
        songs (list): List of songs, probably made by parse()
    """
    with open('songs.txt', 'w', encoding="UTF-8") as songsFile:
        for track in songs:
            songsFile.write(f"{track}\n")

def artists(sjsonfile, index):
    """Generates a string with a list of artists in a given index in a sjson.

    Args:
        sjsonfile (string): Entire sjson from Spotify
        index (int): Index of the track from which will be extracted the artists

    Returns:
        string: A string containing a list of the song's artists separated by a space
    """
    artists = ""
    for art in json.loads(sjsonfile)[index]['track']['artists']:
        artists += " " + art['name']
    return artists