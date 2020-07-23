"""Downloads the actual files from a txt"""

import youtube_dl
import os
import pathlib
import re

cwd = os.getcwd()

def download(search):
    """Downloads from YouTube based on a search

    Args:
        search (list): A list of search queries with the song's title separated by its artists
    """
    if not song_exists(search[0]):
        try:
            ydl_opts = {
                "format" : "bestaudio/best",
                "postprocessors": [{
                    "key" : "FFmpegExtractAudio",
                    'preferredcodec': 'mp3',
                    'preferredquality': '192'
                }],
                "outtmpl" : f"{cwd}/songs/%(title)s.%(ext)s"
            }
            with youtube_dl.YoutubeDL(params=ydl_opts) as ydl:
                ydl.download([f'ytsearch1:{search[0]} {search[1]} song'])
        except:
            pass

def download_list(searches):
    """Downloads from YouTube based on a list of search queries

    Args:
        searches (list): List of strings containing search queries
    """
    for song in searches:
        download(song)

def song_exists(songName):
    """Checks if a song already exists in songs' path

    Args:
        songName (string): The name of the song that will be searched

    Returns:
        boolean: If the song already exists or not
    """
    pattern = re.compile(songName.lower())
    for filename in os.listdir("songs/"):
        if re.search(pattern, filename.lower()):
            return True
    return False