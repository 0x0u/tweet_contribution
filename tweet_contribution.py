import tweepy,requests,datetime
from bs4 import BeautifulSoup as bs

def get_contribution():
    url = 'https://github.com/users/' + your_git_hub_id  + '/contributions'
    req = requests.get(url)
    soup = bs(req.content,'html.parser')
    contribution = [i.get('data-count') for i in soup.find_all(class_="day")]
    return contribution[-1]

def tweet(text):
    consumer_key = 'consumer_key'
    consumer_secret = 'consumer_secret'
    access_key = 'access_key'
    access_secret = 'access_secret'
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    api.update_status(text)

if __name__ == '__main__':
    day = datetime.date.today()
    num = get_contribution()
    text = '{}のcontribution数は{}でした #github'.format(day,num)
    tweet(text)

