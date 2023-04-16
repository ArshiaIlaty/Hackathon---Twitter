import pandas as pd
from textblob import TextBlob
import json
from matplotlib import pyplot as plt
from translate import translate, run_translate

def sentiment_analysis(username: str):
    full_path = './users/' + username + '.csv'
    df = pd.read_csv(full_path)
    df.columns = ['Tweet_id', 'Username', 'Name', 'Profile_picture', 'Replies', 'Retweets', 'Likes', 'Is_retweet', 'Posted_time', 'Content', 'Hashtags', 'Mentions', 'Images', 'Videos', 'Tweet_url', 'Link']

    def getSubjectivity(text):
        try:
            return TextBlob(text).sentiment.subjectivity
        except:
            return None

    def getPolarity(text):
        try:
            return TextBlob(text).sentiment.polarity
        except:
            return None

    df['subjectivity'] = df['Content'].apply(getSubjectivity)
    df['polarity'] = df['Content'].apply(getPolarity)

    def getAnalysis(score):
        if score < 0:
            return 'Negative'
        elif score == 0:
            return 'Neutral'
        else:
            return 'Positive'
    df['analysis'] = df['polarity'].apply(getAnalysis)
    df = df.dropna()
    sentiment_counts = df.groupby(['analysis']).size()
    df = json.loads(df.to_json(orient='records'))

    #visualize the sentiments
    # fig = plt.figure(figsize=(6,6), dpi=100)
    # ax = plt.subplot(111)
    # sentiment_counts.plot.pie(ax=ax, autopct='%1.1f%%', startangle=270, fontsize=12, label="")

    return df