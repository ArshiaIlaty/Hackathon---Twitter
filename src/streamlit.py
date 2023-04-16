# import streamlit as st
# import pandas as pd
# import tweepy
# # from PIL import Image, ImageDraw, ImageFont
# import requests

# # Twitter API credentials
# consumer_key = "your_consumer_key"
# consumer_secret = "your_consumer_secret"
# access_token = "your_access_token"
# access_token_secret = "your_access_token_secret"

# # Authenticate to Twitter API
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
# api = tweepy.API(auth)

# # Define Twitter handle and tweet ID
# twitter_handle = "arshiailaty"
# tweet_id = "1647371620087140352"

# # Get tweet details
# tweet = api.get_status(tweet_id, tweet_mode="extended")

# # Extract media URLs from tweet
# media = tweet.entities.get("media", [])
# if len(media) > 0:
#     media_url = media[0]["media_url"]
# else:
#     st.error("No media found in tweet.")

# # Download and display media
# response = requests.get(media_url)
# img = Image.open(BytesIO(response.content))
# st.image(img, caption="Twitter GIF")

# # Load CSV file
# csv_file = "./src/users/arshiailaty.csv"
# df = pd.read_csv(csv_file)

# # Display CSV file
# st.write(df)

import time

import numpy as np
import pandas as pd

import streamlit as st

# import shapefile

st.empty()
my_bar = st.progress(0)
for i in range(100):
    my_bar.progress(i + 1)
    time.sleep(0.1)
n_elts = int(time.time() * 10) % 5 + 3
for i in range(n_elts):
    st.text("." * i)
st.write(n_elts)
for i in range(n_elts):
    st.text("." * i)
st.success("done")