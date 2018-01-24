

# tweetharvester

Twitter stores tweets as Status objects.  

After adding all the code necessary to look for tweets and extract various parts, 
now I am going to add code to analyse the Lexical diversity of the returned tweets.  
  
## Lexical Diversity
Lexical diversity is a measure of how many unique words are used in a text. It can be be used in interpersonal communication in determining how rich or otherwise someone’s use of language is. It can also be used in social media to determine how broadly a topic is being discussed.

## Tweet Popularity
This will cover the following:
 1. Determine how popular a tweet is by counting its number of retweets.
 2. Set a retweet threshold value that ignores retweets below a certain number.
 3. Prettify the results by listing the text of the popular tweets alongside its retweet,  
    and order the list by popularity.  
    
    
## User Info

Twitter stores user information in as User objects.  

With a User object, you can find out things like 
* how many followers an account has, 
* who they are following, and 
* more.

To get some user info on to the screen you’ll use Tweepy’s User model. 
And to get users, you use the get_user method of the API class.