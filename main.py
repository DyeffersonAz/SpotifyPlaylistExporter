"""Module that controls the software, authenticating the user and downloading all of its loved songs in Spotify"""

import spotifier
import json
import tracks_parser
import downloader
from dotenv import load_dotenv
import os

load_dotenv()

print("Vamos começar a baixar suas favoritas, mas primeiro vamos preparar algumas coisas...")

spotifier.auth(os.getenv("USERNAME")) #Authing with Spotify

savedTracks = spotifier.get_saved_tracks() #Getting a list of dictionaries from Spotify
print("Pronto, agora vamos começar a baixar!")
downloader.download_list(tracks_parser.parse(json.dumps(savedTracks))) # Downloads from a list of songs dumped in a json string and parsed by tracks-parser.py
