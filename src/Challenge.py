from flask import Flask, render_template, jsonify
import pymongo
from pymongo import MongoClient
from bson.json_util import dumps
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import tweepy
import datetime
import openai
import csv
from textblob import TextBlob

class MyStreamListener(tweepy.StreamListener):

    def __init__(self, api):
        super().__init__(api)
        self.db = # connect to your database here

    def on_status(self, status):
        if status.in_reply_to_status_id is not None:
            # tweet is a reply
            # check if it is a reply to one of the selected accounts
            # and store the data in your database
            if status.in_reply_to_user_id_str in ["id1", "id2", "id3"]:
                # store the reply in your database
                pass
    def on_error(self, status_code):
        if status_code == 420:
            return False

if __name__ == "__main__":
    consumer_key = "YOUR_CONSUMER_KEY"
    consumer_secret = "YOUR_CONSUMER_SECRET"
    access_token = "YOUR_ACCESS_TOKEN"
    access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    myStreamListener = MyStreamListener(api)
    myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

    # set up a filter for the selected accounts and start streaming
    myStream.filter(follow=["id1", "id2", "id3"], is_async=True, since_id=datetime.datetime(2023, 2, 1))

# initialize sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# define function to calculate sentiment score for a tweet
def get_sentiment_score(tweet):
    # calculate polarity scores for the tweet text
    polarity_scores = analyzer.polarity_scores(tweet)
    # return the compound score, which represents overall sentiment
    return polarity_scores['compound']
    
# define function to calculate sentiment score for a set of tweets
def get_thread_sentiment_score(thread):
    # calculate sentiment score for each tweet in the thread
    sentiment_scores = [get_sentiment_score(tweet['text']) for tweet in thread]
    # return the average sentiment score for the thread
    return sum(sentiment_scores) / len(sentiment_scores)

# define function to calculate sentiment score for a set of replies
def get_audience_sentiment_score(replies):
    # calculate sentiment score for each reply in the set
    sentiment_scores = [get_sentiment_score(reply['text']) for reply in replies]
    # return the average sentiment score for the set
    return sum(sentiment_scores) / len(sentiment_scores)


app = Flask(__name__)

# Connect to MongoDB client
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Retrieve database and collections
db = client["twitter"]
accounts_col = db["accounts"]
threads_col = db["threads"]
audience_col = db["audience"]
sentiment_col = db["sentiment"]

# Endpoint to render the home page
@app.route('/')
def home():
    return render_template('home.html')

# Endpoint to render the accounts page
@app.route('/accounts')
def accounts():
    accounts = accounts_col.find()
    return render_template('accounts.html', accounts=accounts)

# Endpoint to render the threads page for a given twitter handleaf
@app.route('/threads/<twitter_handle>')
def threads(twitter_handle):
    threads = threads_col.find({'twitter_handle': twitter_handle})
    return render_template('threads.html', threads=threads)

# Endpoint to render the audience page for a given twitter handle
@app.route('/audience/<twitter_handle>')
def audience(twitter_handle):
    audience = audience_col.find_one({'twitter_handle': twitter_handle})
    return render_template('audience.html', audience=audience)

# Endpoint to render the sentiment page for a given twitter handle
@app.route('/sentiment/<twitter_handle>')
def sentiment(twitter_handle):
    sentiment = sentiment_col.find_one({'twitter_handle': twitter_handle})
    return render_template('sentiment.html', sentiment=sentiment)

if __name__ == '__main__':
    app.run()
