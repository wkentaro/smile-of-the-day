#!/usr/bin/env python
#-*- coding: utf-8 -*-
# download_img.py

import os
import sha
import urllib


def download_img(url, filename, desc=None):
    img = urllib.URLopener()
    try:
        img.retrieve(url=url, filename=filename)
        return True
    except IOError:
        return False


def test_download_img():
    if not os.path.exists('img'):
        os.mkdir('img')

    url = 'http://inperc.com/wiki/images/f/fb/Lena.jpg'
    filename = 'img/' + sha.sha(url).hexdigest()
    download_img(url=url,
                 filename=filename)


if __name__ == '__main__':
    test_download_img()
