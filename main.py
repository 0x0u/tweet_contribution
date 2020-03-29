import os
import sys
import tweepy
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta, timezone

def get_contribution(gh_id):
    url = "https://github.com/users/" + gh_id + "/contributions"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    return soup.find_all(class_="day")[-1]["data-count"]

def tweet(text):
    consumer_key = os.environ.get("consumer_key")
    consumer_secret = os.environ.get("consumer_secret")
    access_key = os.environ.get("access_key")
    access_secret = os.environ.get("access_secret")
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    api.update_status(text)


if __name__ == "__main__":
    args = sys.argv
    jst = timezone(timedelta(hours=+9), "JST")
    today = datetime.now(jst).strftime("%Y-%m-%d")
    contribution = get_contribution(args[1])
    text = "{}のcontribution数は{}でした #github".format(today, contribution)
    tweet(text)

