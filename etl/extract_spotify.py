import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


import os
from dotenv import load_dotenv
load_dotenv()


def get_spotify_client():
    auth = SpotifyClientCredentials(
        client_id=os.getenv('SPOTIFY_CLIENT_ID'),
        client_secret=os.getenv('SPOTIFY_CLIENT_SECRET')
    )
    return spotipy.Spotify(auth_manager=auth)

def fetch_spotify_tracks(playlist_id):
    sp = get_spotify_client()
    tracks = []
    results = sp.playlist_tracks(playlist_id)
    tracks.extend(results['items'])
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks
