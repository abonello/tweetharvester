import json
import tweepy
from keys_and_secrets import get_auth, twitter_api

# Twitter API authentication keys
api = twitter_api()
auth = get_auth()

user = api.get_user('@madonna')


print "This is the whole data for USER\n"
print json.dumps(user._json, indent=4)
print "============ END USER ============\n\n"
print " SCREEN NAME"
print user.screen_name
print "\n Follower\'s Count"
print user.followers_count
print "============ END USER ============\n\n"

print " FRIENDS: Screen Name and follower's count" 
for friend in user.friends():
    print 
    print friend.screen_name
    print friend.followers_count

'''
We can easily harvest tweets that appear on a user's timeline by invoking the api.home_timeline method.
'''

for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a tweet
    print status.text.encode('utf-8')
