"""Module that controls the software"""

import spotifier
import json
import tracks_parser
import downloader

spotifier.auth("21db2xi7bbketgljwabmna7wa")

savedTracks = spotifier.get_saved_tracks()

with open("tracks.json", 'w') as jsonfile:
    jsonfile.write(json.dumps(savedTracks))
with open("tracks.json", "r") as jsonfile:
    jsonraw = jsonfile.read()

downloader.download_list(tracks_parser.parse(jsonraw))