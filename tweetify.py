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

thread_start = api.get_status("1091073809707352072")
current_tweet = thread_start
song_titles = []
while (current_tweet._json["in_reply_to_status_id_str"]):
    next_id = current_tweet._json["in_reply_to_status_id_str"]
    song_titles.append(current_tweet.text)
    current_tweet = api.get_status(next_id)

song_titles.reverse()
pp.pprint(song_titles)
# print(json.dumps(thread_start._json, indent=4, sort_keys=True))


