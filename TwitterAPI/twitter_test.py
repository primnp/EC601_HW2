import tweepy
import pandas as pd
import os

#twitter API credentials
# consumer_key = "your twitter API key"
# consumer_secret = "your twitter API secret"
# access_key = "your twitter access key"
# access_secret = "your twitter access secret"

def tweepy_api():
    #get secrets from github
    cons_key = os.getenv("CONS_KEY")
    cons_secret = os.getenv("CONS_SECRET")
    accs_key = os.getenv("ACCESS_KEY")
    accs_secret = os.getenv("ACCESS_SECRET")

    #twitter api credentials set up
    auth = tweepy.OAuthHandler(cons_key, cons_secret)
    auth.set_access_token(accs_key, accs_secret)
    api = tweepy.API(auth)
    return api

# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_key, access_secret)
# api = tweepy.API(auth)
api = tweepy_api()

no_of_tweets = 46
tweets = [] #full_text
likes = [] #favorite_count
time = [] #created_at
hashtag = [] #hashtag

#retrieve 46 most recent tweets from a specific user (in this case, it's @danielricciardo)
cursor = tweepy.Cursor(api.user_timeline, id="danielricciardo", tweet_mode="extended").items(no_of_tweets)

for i in cursor:
    tweets.append(i.full_text)
    likes.append(i.favorite_count)
    time.append(i.created_at)
    hash = (i.entities['hashtags'])
    hashtag.append(hash)

#display retrieved information in dataframe format
df = pd.DataFrame({'tweets': tweets, 'likes': likes, 'time': time, 'hashtag': hashtag})
print(df.to_string())
