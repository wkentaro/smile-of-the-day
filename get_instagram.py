#!/usr/bin/env python
# -*- coding: utf-8 -*-
# get_instagram.py

import os
import sha

from instagram.client import InstagramAPI

import load_yaml
import download_img


def get_instagram(key):
    api = InstagramAPI(client_id=key['client_id'],
                       client_secret=key['client_secret'])
    popular_media = api.media_popular(count=20)

    urls = []
    for media in popular_media:
        url = media.images['standard_resolution'].url
        urls.append(url)
    return urls


def test_get_instagram():
    key = load_yaml.load_yaml(sns='instagram')[0]
    urls = get_instagram(key=key)

    # make directory to save imgs
    if not os.path.exists('img'):
        os.mkdir('img')

    for url in urls:
        filename = 'img/' + sha.sha(url).hexdigest()
        download_img.download_img(url=url, filename=filename)


if __name__ == '__main__':
    test_get_instagram()