#!/usr/bin/env python2
import json
import tweepy
from keys_and_secrets import get_auth, twitter_api
from collections import Counter
from prettytable import PrettyTable
from operator import itemgetter

# Twitter API authentication keys
api = twitter_api()
auth = get_auth()

count = 10
query = 'Brexit'
#query = 'Ireland'


# Get all tweets for the search query
# list comprehension using the api.search object based on the query value
results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

'''
min_rewtweets variable acts as a threshold.
Any tweets with a retweet count less than or equal to the value assigned 
will be ignored. Basically, you can determine what level of retweets are 
required for a tweet to be considered popular.
'''
min_retweets = 10  # the min amount of times a status is retweeted to gain entry to our list.
                   # reset this value to suit your own tests
                   
'''
As you loop through the result set of tweets from the search, you check 
if the retweet_count is greater than the threshold. If it is, it gets 
added to the pop_tweets list.
'''
pop_tweets = [status                   # building a list
              for status in results
              if status._json['retweet_count'] > min_retweets]

print "\n LIST OF POPULAR TWEETS"
print pop_tweets
print "\n\n\n ORGANISED as JSON"

for i in range(len(pop_tweets)):
    print json.dumps(pop_tweets[i]._json, indent=4)
    

'''
Then add the tweet text and retweet_count values for each entry in the pop_tweets 
list into a new list of tuples called tweet_tups. This serves to isolate the 
values so you can sort them in order of popularity.
Assign the five most popular tweet tuples in this list to another list while 
sorting on the retweet_count located at index 1 for each tuple entry -- 
key=itemgetter(1). Note that reverse=True means sorting in descending order.
'''

# create a list of tweet tuples associating each tweet's text with its retweet count
tweet_tups = [(tweet._json['text'].encode('utf-8'), tweet._json['retweet_count'])
              for tweet in pop_tweets]

# Sort the tuple entries in descending order
most_popular_tups = sorted(tweet_tups, key=itemgetter(1), reverse=True)[:5]

print "\n\n This is a tuplet of TEXT and RETWEET_COUNT"
print tweet_tups


'''
Finally, add this list of tuples containing the 5 most popular tweets to a 
pretty table for console output formatting. Notice the text column width is 
limited to 50 characters to fit on the page.
'''

# prettify
table = PrettyTable(field_names=['Text', 'Retweet Count'])
for key, val in most_popular_tups:
    table.add_row([key, val])
    table.add_row(["", ""]) # add empty row between data
table.max_width['Text'] = 50
table.align['Text'], table.align['Retweet Count'] = 'l', 'r' # align the columns
print "\n\n\n" # create some space before the table
print table