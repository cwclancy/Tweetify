import pprint
import sys
import os
import subprocess 

import spotipy
import spotipy.util as util

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
    playlists = sp.user_playlist_create(username, "test", public=True, description="test")
    print(playlists)
else:
    print("Can't get token for", username)
