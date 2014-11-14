#-*- coding:utf-8 -*-
import tweepy
import os

consumer_key = "7vBUMmund9P7okUW4mu6VEjWh"
consumer_secret = "Jh3XL273ScX20pGEfzShMpGxMMRbbSsjYnTxpBMbuponzp4Y14"
access_token = "1725144152-XGTkVKMlUXiYk49HJ0RXSB6PIM6VYxh5M2KScKW"
access_token_secret = "GcmboN0QSiofWbKFSEjb77Sgxz3luglyeY3XdGxOkJq1p"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

media_tweet_urls = []
for tweet in list(tweepy.Cursor(api.user_timeline).items()):
        if 'entities' in tweet.__dict__:
                    if 'media' in tweet.__dict__['entities']:
                                    media_tweet_urls.append(tweet.entities['media'][0]['media_url'])

# print(media_tweet_urls)
for url in media_tweet_urls:
    os.system('wget {}'.format(url))
