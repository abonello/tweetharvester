import json
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