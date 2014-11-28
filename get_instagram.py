#! /usr/bin/env python
# -*- coding: utf-8 -*-
# instagram.py

import requests
from instagram.client import InstagramAPI

import load_yaml


def get_instagram(key):
    api = InstagramAPI(client_id=key['client_id'],
                       client_secret=key['client_secret'])
    popular_media = api.media_popular(count=20)
    for media in popular_media:
        img_url = media.images['standard_resolution'].url
        print img_url


def main():
    key = load_yaml.load_yaml(sns='instagram')[0]
    data = get_instagram(key=key)


if __name__ == '__main__':
    main()