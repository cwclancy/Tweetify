import tweepy
import json
import pprint

pp = pprint.PrettyPrinter(indent=4)

consumer_key = "ZMStQd7o698CXe1kbb9K7pmQN"
consumer_secret = "S6kzYrIREWCxnRX00erOHF4TWxbhNduBdlQbvj1al9EnuVqWAU"

access_token = "1363296206-OhazXflCmmRZgCdIv8nbHaE2XYiQbsWDwspNmgm"
access_secret = "YSvDkxc65e08cR2uFtjc19cl8tYWxNwN1LNjxk23XfBOH"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

status_id = "1091073809707352072"

def get_thread(thread_start):
    current_tweet = api.get_status(thread_start)
    song_titles = []
    while (current_tweet._json["in_reply_to_status_id_str"]):
        next_id = current_tweet._json["in_reply_to_status_id_str"]
        song_titles.append(current_tweet.text)
        current_tweet = api.get_status(next_id)
    song_titles.reverse()
    return song_titles

def find_start_index(song_arr):
    return 1

def find_end_index(song_arr):
    for i in range(len(song_arr)):
        if song_arr[i] == "-":
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


pp.pprint(clean_thread(get_thread(status_id)))


