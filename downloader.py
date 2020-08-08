"""Downloads the actual files from a txt"""

import youtube_dl
import os
import pathlib
import re

cwd = os.getcwd()

def download(search, directory=f"{cwd}/songs"):
    """Downloads from YouTube based on a search

    Args:
        search (list): A list of search queries with the song's title separated by its artists
        directory (string, optional): A string of the directory where the song will be put
    """
    if not song_exists(search[0], directory=directory):
        try:
            ydl_opts = {
                "format" : "bestaudio/best",
                "postprocessors": [{
                    "key" : "FFmpegExtractAudio",
                    'preferredcodec': 'mp3',
                    'preferredquality': '192'
                }],
                "outtmpl" : f"{directory}/%(title)s.%(ext)s"
            }
            with youtube_dl.YoutubeDL(params=ydl_opts) as ydl:
                ydl.download([f'ytsearch1:{search[0]} {search[1]} song'])
        except:
            pass

def download_list(searches, directory=f"{cwd}/songs"):
    """Downloads from YouTube based on a list of search queries

    Args:
        searches (list): List of strings containing search queries
        directory (string, optional): A string of the directory where the songs will be put
    """
    for song in searches:
        download(song, directory=directory)

def song_exists(songName, directory="songs/"):
    """Checks if a song already exists in songs' path

    Args:
        songName (string): The name of the song that will be searched
        directory (string, optional): A string of the directory where the songs will be searched on

    Returns:
        boolean: If the song already exists or not
    """
    pattern = re.compile(songName.lower())
    for filename in os.listdir(directory):
        if re.search(pattern, filename.lower()):
            return True
    return False