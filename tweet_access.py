import json
import tweepy
from keys_and_secrets import get_auth, twitter_api

# Twitter API authentication keys
api = twitter_api()
auth = get_auth()

count = 10
query = 'Dublin'

# Get all status
results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

for result in results:
    print result
    print "\n"
