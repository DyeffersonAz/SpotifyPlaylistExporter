"""Module that controls the software"""

import spotifier
import json
import tracks_parser
import downloader
import configparser

cnfg = configparser.ConfigParser()

cnfg.read("config.cfg")

spotifier.auth(cnfg.get("SPOTIFY", "USERNAME"))

savedTracks = spotifier.get_saved_tracks()

downloader.download_list(tracks_parser.parse(json.dumps(savedTracks)))