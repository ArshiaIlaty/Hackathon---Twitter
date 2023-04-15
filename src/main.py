from fastapi import FastAPI
from scrape_profile_tweets import scrape_profile_tweets_since_2023
from starlette.responses import RedirectResponse

description = """
Twitter Tracker 🚀

## Accounts

You can **read accounts**.

## Tweets

You will be able to:

* **Tweets of the user** (_implemented_).
* **audience: Active users by the number of their mentions** (_implemented_).
* **sentiment: sentiment of each mention** (_implemented_).
* **replies: get the replies of each tweet** (_implemented_).
"""

app = FastAPI(
    title="Twitter Watch",
    description=description,
    version="0.0.1",
    terms_of_service="https://www.instagram.com/arshia_ilaty/",
    contact={
        "name": "Arshia Ilaty",
        "url": "https://www.linkedin.com/in/arshia-ilaty/",
        "url": "https://github.com/ArshiaIlaty",
        "email": "arshia.ilaty99@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

@app.get("/tweets/{twitter_handle}")
async def tweets(twitter_handle):
    res = scrape_profile_tweets_since_2023(twitter_handle)
    return res

@app.get("/")
async def hello():
    return RedirectResponse(url='/docs')


if __name__ == '__main__':
    app.run()