import json
import tweepy
from keys_and_secrets import get_auth, twitter_api

# Twitter API authentication keys
api = twitter_api()
auth = get_auth()

count = 10
query = 'Dublin'

# Get all status
# list comprehension using the api.search object based on the query value
results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

# for result in results:
#     print result
#     print

print "\n\n ORGANISED \n"

# for result in results:
#     print json.dumps(result._json, indent=2)

print json.dumps(results[0]._json, indent=4)

print "\n\n ***** SELECTED DATA *****"

for status in results:
    print status.text.encode('utf-8')
    print status.user.id
    print status.user.screen_name
    print status.user.profile_image_url_https
    print status.user.followers_count
    print status.place
    print



