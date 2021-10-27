import tweepy
import time
import json
import pandas as pd
import logging
import sys
import os
from google.cloud import language_v1

# #twitter API credentials
# consumer_key = "your twitter API key"
# consumer_secret = "your twitter API secret"
# access_key = "your twitter access key"
# access_secret = "your twitter access secret"
#
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_key, access_secret)
# api = tweepy.API(auth)

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

# Instantiates a client
client = language_v1.LanguageServiceClient()

# Logging error
logging.basicConfig(filename="calc.log", level=logging.DEBUG, format="[%(levelname)s] %(asctime)s %(message)s")

# function to retrieve information from twitter user
def twitter_retrieve(text, number):
    api = tweepy_api()
    if type(text) is str and type(number) is int and number < 200:
        tweets_data = []
        cursor = tweepy.Cursor(api.user_timeline, screen_name=text, tweet_mode="extended").items(number)
        for i in cursor:
            res = dict()
            res["Tweets"] = i.full_text
            res["Likes"] = i.favorite_count
            res["Time"] = i.created_at
            hash = (i.entities['hashtags'])
            res["Hashtags"] = hash
            tweets_data.append(res)

        logging.info("Twitter user data extracted")

        return tweets_data

    else:
        logging.error("Error extracting twitter user data")
        return[]

# function to retrieve sentiments from user's tweets
def entities_sentiments_retrieve(array):
    if isinstance(array, list):

        # initialize the array to insert dictionary of entity,sentiment
        results = []

        # initialize array to categorize dictionary of entity,sentiment per tweet as well as tweet posted time and number of likes
        fin_results = []

        for i in range(len(array)):
            twt_extracted_dat = dict()

            text = array[i]["Tweets"]

            document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)

            # Detects the entity and sentiment of the text
            response = client.analyze_entity_sentiment(request={'document': document})

            for ent in response.entities:
                res = dict()
                res["Entity"] = ent.name
                res["SentimentScore"] = ent.sentiment.score * ent.sentiment.magnitude
                results.append(res)

            twt_extracted_dat["Tweet text"] = array[i]["Tweets"]
            twt_extracted_dat["Tweet Entities"] = results
            twt_extracted_dat["Twitter's Likes"] = array[i]["Likes"]
            twt_extracted_dat["Twitter's Posted Time"] = array[i]["Time"]

            hash = array[i]["Hashtags"]
            twt_extracted_dat["Twitter's Hashtags"] = hash

            fin_results.append(twt_extracted_dat)

        logging.info('Sentiments analyzed')

        return fin_results

    else:
        logging.error("Error analyzing sentiment")
        return []

# # function to gather all hashtag from users
# def hashtags_retrieve(array)
#     if isinstance(array, list):
#         for i in range(len(array)):
#             text = array[i]["Hashtags"]
#             for j in range(len(text)):
#                 hash = array[i]["Hashtags"][j]["text"]


# function to retrieve text from hashtag
def txt_hashtag_retrieve(text, array):
    if type(text) is str and type(array) is list:
        results = []
        for i in range(len(array)):
            hash_arr = array[i]["Twitter's Hashtags"]
            for j in range(len(hash_arr)):
                hash = array[i]["Twitter's Hashtags"][j]["text"]
                if hash == text:
                    twitter_txt = array[i]["Tweet text"]
                    results.append(twitter_txt)

        logging.info('Hashtag found')

        return results

    else:
        logging.error("Hashtag not found")
        return []
