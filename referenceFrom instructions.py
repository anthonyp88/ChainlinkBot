#!/root/anaconda3/bin/python
import tweepy           # To consume Twitter's API
import pandas as pd     # To handle data
import numpy as np      # For number computing
import sys
from slacker import Slacker
# For plotting and visualization:
from IPython.display import display
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
from datetime import timezone
import re
from credentials import *    # This will allow us to use the keys as variables

# Twitter App access keys for @user

# Consume:
CONSUMER_KEY = 'CONSUMER_KEY'
CONSUMER_SECRET = 'CONSUMER_SECRET'

# Access:
ACCESS_TOKEN = 'ACCESS_TOKEN'
ACCESS_SECRET = 'ACCESS_SECRET'
slack = Slacker('xoxb-FSGSF-DFSGFSG-FGFGDF')

# API's setup:
# inp = [{'client': 'epic', 'domain': 'fnwp', 'twittername': 'Rainbow6Game'}, {'client': 'epic1', 'domain': 'fnwp1', 'twittername': 'abhi98358'}, {
#   'client': 'epic', 'domain': 'fnwp', 'twittername': 'Rainbow6Game'}, {'client': 'abhi', 'domain': 'abhi', 'twittername': 'FortniteGame'}]
#dff = pd.DataFrame(inp)
dff = pd.read_csv("twitter.csv")


def twitter_setup():
    """
    Utility function to setup the Twitter's API
    with our access keys provided.
    """
    # Authentication and access using keys:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    # Return API with authentication:
    api = tweepy.API(auth)
    return api


for index, row in dff.iterrows():
    twt = row['twittername']
    domain = row['domain']
    extractor = twitter_setup()
    # We create a tweet list as follows:
    tweets = extractor.user_timeline(screen_name=twt, count=200)
    data = pd.DataFrame(
        data=[tweet.text for tweet in tweets], columns=['Tweets'])

    # We add relevant data:
    data['ID'] = np.array([tweet.id for tweet in tweets])
    data['Date'] = np.array([tweet.created_at for tweet in tweets])
    data['text'] = np.array([tweet.text for tweet in tweets])
    #data['Date'] = pd.to_datetime(data['Date'], unit='ms').dt.tz_localize('UTC').dt.tz_convert('US/Eastern')
    data = data[~data["Tweets"].str.contains("@")]
    created_time = datetime.datetime.utcnow() - datetime.timedelta(minutes=1)

    data = data[(data['Date'] > created_time) & (
        data['Date'] < datetime.datetime.utcnow())]

    my_list = ['SALE', 'OFFER', 'downtime']

    #ndata = data[data['Tweets'].str.contains( "|".join(my_list), regex=True)].reset_index(drop=True)
    ndata = data[data['Tweets'].str.contains(
        "|".join(my_list), regex=True, flags=re.IGNORECASE)].reset_index(drop=True)

    # print(ndata)
    if len(ndata['Tweets']) > 0:
        slack.chat.post_message('#ops-twitter-alerts',
                                domain + ': ' + ndata['Tweets'] + '<!channel|>')
    else:
        print('hi')
