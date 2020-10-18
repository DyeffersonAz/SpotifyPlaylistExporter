import random
import string
import base64
import configparser
import webbrowser
import socket
import pathlib

cfg = configparser.ConfigParser()
cfg.read(pathlib.PureWindowsPath("credentials.cfg"))


def genCode(length):
    return ''.join(random.SystemRandom().choices(string.ascii_lowercase + string.ascii_uppercase + "0123456789" + "~_.-", k=length))

def openLocalPort():
    PORT = 8888
    socket.bind(('localhost', PORT))

def getToken():
    verifier = genCode(128)
    challenge = str(base64.b64encode(verifier.encode("utf-8")), "utf-8")
    client_id = cfg.get("SPOTIFY", "CLIENT_ID")
    response_type = "code"
    redirect_uri = cfg.get("SPOTIFY", "REDIRECT_URI")
    code_challenge_method = "S256"
    state = genCode(random.randint(5, 15))
    scope = "playlist-read-private"
    webbrowser.open(f"https://accounts.spotify.com/authorize?response_type={response_type}&client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}&state={state}&code_challenge={challenge}&code_challenge_method={code_challenge_method}")

def auth_user():
    getToken()

auth_user()