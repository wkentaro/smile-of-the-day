#-*- coding:utf-8 -*-
import tweepy
import os

import load_yaml


def get_twitter(key):
    auth = tweepy.OAuthHandler(key['consumer_key'],
                               key['consumer_secret'])
    auth.set_access_token(key['access_token'],
                          key['access_token_secret'])

    api = tweepy.API(auth)

    tweets = tweepy.Cursor(api.user_timeline)

    usable_tweets = []
    for tweet in tweets.items():
        if 'entities' not in tweet.__dict__:
            continue
        elif tweet.coordinates is None:
            continue

        if 'media' in tweet.__dict__['entities']:
            media_url = tweet.entities['media'][0]['media_url']
            coordinates = tweet.coordinates['coordinates']
            tw_info = dict(media_url=media_url, coordinates=coordinates)
            usable_tweets.append(tw_info)

    for tw_info in usable_tweets:
        media_url = tw_info['media_url']
        coordinates = tw_info['coordinates']
        os.system('wget --quiet {0}'.format(media_url))
        print coordinates


def main():
    api_keys = load_yaml.load_yaml(sns='twitter')
    for key in api_keys:
        get_twitter(key=key)


if __name__ == '__main__':
    main()
