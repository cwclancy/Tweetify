# Connor Clancy - cclancy@andrew.cmu.edu
# Spotter - 
#   Spotify utility functions based around the spotify API wrapper Spotipy
#   Requires a spotify dev account and auth stuff from spotify
#   utility functions include:
#           new_playlist, get_song_ids, add_songs_to_playlist

import pprint
import sys
import os
import subprocess 

import spotipy
import spotipy.util as util


username = "1259558123" # given by Spotify - can be found by going to one of your created playlists
                        # and going to share and copying Spotify URI 

scope = 'playlist-modify-public' # scope variable for token
token = util.prompt_for_user_token(username, scope, # auth token
                                   client_id="08eadc5689f94a85b24cfe5f147b4eef",
                                   client_secret="7ff1dc7f25ad4bb18162d210cefe01ab",
                                   redirect_uri='http://localhost:8888/callback/')
if token:
    sp = spotipy.Spotify(auth=token)
else:
    raise "Failed to bind token"

## new_playlist: string playlist_name * string playlist_description -> string playlist_id
# string playlist_name - name of your new Spotify playlist
# string playlist_description - description of your new Spotify Playlist
# string playlist_id - Spotify given playlist id of your newly created playlist

def new_playlist(playlist_name, playlist_description):
    global username
    global sp
    playlist = sp.user_playlist_create(username, playlist_name, public=True, 
                                       description=playlist_description)
    return playlist["id"]

## get_song_id: string song -> string song_id
# string song - name of the song you want the Spotify song_id for
# string song_id - Spotify given song_id

def get_song_id(song):
    tracks = sp.search(q="track: " + song, type="track")
    if not tracks:
        return None
    else:
        return tracks['tracks']['items'][0]['id']

## get_song_ids: string list songs -> string list song_ids
# string list song -> list of song titles
# string list song_ids -> list of Spotify given song_ids

def get_song_ids(songs):
    song_ids = []
    for song in songs:
        song_ids.append(get_song_id(song))
    return song_ids

## add_songs_to_playlists: string playlist_id * string list song_ids -> ()
# string playlist_id - Spotify given id of a playlist
# string list song_ids - Spotify given song_ids you want to add to playlist
# () - Updates your Spotify playlists with songs

def add_songs_to_playlist(playlist_id, song_ids):
    global token
    global username
    global sp
    playlist = sp.user_playlist_add_tracks(username, playlist_id, song_ids)
    


