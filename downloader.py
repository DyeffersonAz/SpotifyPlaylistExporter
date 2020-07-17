"""Downloads the actual files from a txt"""

import youtube_dl
import os
import pathlib

cwd = os.getcwd()
print(cwd)

def download(search):
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
            ydl.download([f'ytsearch1:{search} song'])
    except:
        pass

def download_list(songs):
    for song in songs:
        download(song)
