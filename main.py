"""Module that controls the software, authenticating the user and downloading all of its loved songs in Spotify"""

import spotifier
import json
import tracks_parser
import downloader
import configparser

def getSongs(userID, directory):
    spotifier.auth(userID)
    savedTracks = spotifier.get_saved_tracks()
    downloader.download_list(tracks_parser.parse(json.dumps(savedTracks)), directory=directory)



def main():
    print("We'll download your songs, we only need to set some things up first...")
    cnfg = configparser.ConfigParser()

    cnfg.read("config.cfg")

    spotifier.auth(cnfg.get("SPOTIFY", "USERNAME")) #Authing with Spotify

    savedTracks = spotifier.get_saved_tracks() #Getting a list of dictionaries from Spotify
    print("Alright, now we'll start downloading!")
    downloader.download_list(tracks_parser.parse(json.dumps(savedTracks))) # Downloads from a list of songs dumped in a json string and parsed by tracks-parser.py

if __name__ == "__main__":
    main()