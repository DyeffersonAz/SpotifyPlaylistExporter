"""Parses json spotify files into lists of tracks and lists of artists"""

import json

def parse(sjsonfile):
    jsonfile = json.loads(sjsonfile)
    songs = []
    for track in jsonfile:
        songs.append(f"{track['track']['name']} {track['track']['artists'][0]['name']}")
    return songs

def list_into_file(songs):
    with open('songs.txt', 'w', encoding="UTF-8") as songsFile:
        for track in songs:
            songsFile.write(f"{track}\n")