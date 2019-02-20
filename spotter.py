import pprint
import sys
import os
import subprocess 

import spotipy
import spotipy.util as util

test_song_ids = ["2wCVpdNSHjqIn2en8jAnF0"]

username = "1259558123"
playlist_name = "TESTING...."
playlist_description = "did this work?"

scope = 'playlist-modify-public'
token = util.prompt_for_user_token(username, scope, 
                                   client_id="08eadc5689f94a85b24cfe5f147b4eef",
                                   client_secret="7ff1dc7f25ad4bb18162d210cefe01ab",
                                   redirect_uri='http://localhost:8888/callback/')
if token:
    sp = spotipy.Spotify(auth=token)
else:
    raise "Failed to bind token"

def create_playlist(playlist_name, playlist_description):
    global username
    global sp
    playlist = sp.user_playlist_create(username, playlist_name, public=True, 
                                       description=playlist_description)
    return playlist["id"]

def get_song_id(song):
    tracks = sp.search(q="track: " + song, type="track")
    if not tracks:
        return None
    else:
        return tracks['tracks']['items'][0]['id']

def get_song_ids(songs):
    song_ids = []
    for song in songs:
        song_ids.append(get_song_id(song))
    return song_ids


def add_songs_to_playlist(playlist_id, song_ids):
    global token
    global username
    global sp
    playlist = sp.user_playlist_add_tracks(username, playlist_id, song_ids)
    


print(get_song_id("Lose yourself"))
