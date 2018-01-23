import json
import tweepy
from keys_and_secrets import get_auth, twitter_api
from collections import Counter
from prettytable import PrettyTable

# Twitter API authentication keys
api = twitter_api()
auth = get_auth()

#count = 10
#query = 'Dublin'
count = 50
#query = 'Weather'
query = 'Brexit'


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

status_texts = [status._json['text'] for status in results]

screen_names = [status._json['user']['screen_name']
                for status in results
                for mention in status._json['entities']['user_mentions']]

hashtags = [hashtag['text']
            for status in results
            for hashtag in status._json['entities']['hashtags']]

words = [word
         for text in status_texts
         for word in text.split()]




print json.dumps(status_texts[0:5], indent=1)
print json.dumps(screen_names[0:5], indent=1)
print json.dumps(hashtags[0:5], indent=1)
print json.dumps(words[0:5], indent=1)


print "\n\n ***** SELECTED DATA *****"

for status in results:
    print status.text.encode('utf-8')
    print status.user.id
    print status.user.screen_name
    print status.user.profile_image_url_https
    print status.user.followers_count
    print status.place
    print

print "\n\n ***** *****"
for entry in [screen_names, hashtags, words]:
    counter = Counter(entry)
    print counter.most_common()[:10] # the top 10 results
    print

# The following code will print the data in a table format
print " \n\nUsing PrettyTable to prettify the output using a table format"
print " *************************************************************\n"
for label, data in (('Text', status_texts),
                    ('Screen Name', screen_names),
                    ('Word', words)):
    table = PrettyTable(field_names=[label, 'Count'])
    counter = Counter(data)
    [ table.add_row(entry) for entry in counter.most_common()[:10] ]
    table.align[label], table.align['Count'] = 'l', 'r' # align the columns
    print table