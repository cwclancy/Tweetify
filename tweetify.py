# Connor Clancy - cclancy@andrew.cmu.edu
# Tweetify -
#   Twitter utility function based around the twitter API wrapper Tweepy
#   Requires a twitter dev account and auth stuff from twitter
#   main functions:
#       get_thread, create_playlist

import tweepy
import json
import pprint
import spotter

pp = pprint.PrettyPrinter(indent=4)

## Twitter given auth stuff
consumer_key = "ZMStQd7o698CXe1kbb9K7pmQN"
consumer_secret = "S6kzYrIREWCxnRX00erOHF4TWxbhNduBdlQbvj1al9EnuVqWAU"

access_token = "1363296206-OhazXflCmmRZgCdIv8nbHaE2XYiQbsWDwspNmgm"
access_secret = "YSvDkxc65e08cR2uFtjc19cl8tYWxNwN1LNjxk23XfBOH"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

status_id = "1091073809707352072" # last tweet id in thread (end # of url on desktop)


## get_thread: string thread_start -> string list thread_text
# thread_start - tweet id of the last element in the thread that you want
# thread_text - a list of the text from each tweet

def get_thread(thread_start):
    current_tweet = api.get_status(thread_start)
    song_titles = []
    while (current_tweet._json["in_reply_to_status_id_str"]):
        next_id = current_tweet._json["in_reply_to_status_id_str"]
        song_titles.append(current_tweet.text)
        current_tweet = api.get_status(next_id)
    song_titles.reverse()
    return song_titles

## find_start_index: text_arr -> index
# text_arr - the text of a tweet split by " "
# index - position of beginning of song title

def find_start_index(text_arr):
    return 1

## find_end_index: text_arr -> index
# text_arr - the text of a tweet split by " "
# index - position of end of song title

def find_end_index(text_arr):
    for i in range(len(text_arr)):
        if text_arr[i] == "-":
            return i
    return 0

def clean_song(song):
    song_title = ""
    song_arr = song.split(" ")
    start_index = find_start_index(song_arr)
    end_index = find_end_index(song_arr)
    song_title = " ".join(song_arr[start_index:end_index])
    return song_title

def clean_thread(song_thread):
    for i in range(len(song_thread)):
        if i == 3:
            song_thread[i] = "Lose yourself"
        else:
            song_thread[i] = clean_song(song_thread[i])
    for song in song_thread:
        if not song:
            song_thread.remove("")
    return song_thread

def create_playlist(thread_start, playlist_name, playlist_description):
    playlist_id = spotter.new_playlist(playlist_name, playlist_description)
    song_titles = clean_thread(get_thread(thread_start))
    song_ids = spotter.get_song_ids(song_titles)
    spotter.add_songs_to_playlist(playlist_id, song_ids)
    print("Your playlist: " + playlist_name + " was created")


create_playlist(status_id, "Playlist Name", "Playlist Description")

