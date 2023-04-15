import datetime
import pytz

from twitter_scraper_selenium import scrape_keyword
import json
import pandas as pd
import asyncio

def scrape_profile_tweets_since_2023(username: str):
    kword = "from:" + username
    path = './users/' + username
    file_path = path + '.csv'
    tweets = scrape_keyword(
                            headless=False,
                            keyword=kword,
                            browser="chrome",
                            tweets_count=100, # Just 2 tweets to test it and see results faster
                            filename=path,
                            output_format="csv",
                            since="2023-01-01",
                            # until="2025-03-02", # Until Right now
                            )
    data = pd.read_csv(file_path)
    # # Convert Posted_time column from GMT to Pacific time
    pacific_tz = pytz.timezone('US/Pacific')
    data['Posted_time'] = pd.to_datetime(data['Posted_time'], utc=True).dt.tz_convert(pacific_tz).dt.strftime('%Y-%m-%d %H:%M:%S %Z')
    data['Posted_time_gmt'] = pd.to_datetime(data['Posted_time'])
    data['Posted_time_pst'] = pd.to_datetime(data['Posted_time_gmt'], utc=True).dt.tz_convert(pacific_tz)
    data['Posted_time_gmt'] = data['Posted_time_gmt'].dt.strftime('%Y-%m-%d %H:%M:%S %Z')
    data['Posted_time_pst'] = data['Posted_time_pst'].dt.strftime('%Y-%m-%d %H:%M:%S %Z')
    # pacific_tz = pytz.timezone('US/Pacific')
    # data['Posted_time'] = pd.to_datetime(data['Posted_time'], utc=True).dt.tz_convert(pacific_tz)
    # data['Posted_time'] = data['Posted_time'].dt.strftime('%Y-%m-%d %H:%M:%S %Z')

    data = json.loads(data.to_json(orient='records'))
    return data