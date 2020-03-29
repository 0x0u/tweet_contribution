import os
import sys
import tweepy
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta, timezone

# githubのID
GH_ID = sys.argv[1]

# Tokens
CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET")

def get_contribution():
    url = "https://github.com/users/" + GH_ID + "/contributions"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    return soup.find_all(class_="day")[-1]["data-count"]

def tweet(text):
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    api.update_status(text)


if __name__ == "__main__":
    jst = timezone(timedelta(hours=+9), "JST")
    today = datetime.now(jst).strftime("%Y-%m-%d")
    contribution = get_contribution()
    text = "{}のcontribution数は{}でした #github".format(today, contribution)
    tweet(text)

