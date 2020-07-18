"""Module that controls the software, authenticating the user and downloading all of its loved songs in Spotify"""

import spotifier
import json
import tracks_parser
import downloader
import configparser

cnfg = configparser.ConfigParser()

cnfg.read("config.cfg")

spotifier.auth(cnfg.get("SPOTIFY", "USERNAME")) #Authing with Spotify

savedTracks = spotifier.get_saved_tracks() #Getting a list of dictionaries from Spotify

downloader.download_list(tracks_parser.parse(json.dumps(savedTracks))) # Downloads from a list of songs dumped in a json string and parsed by tracks-parser.py