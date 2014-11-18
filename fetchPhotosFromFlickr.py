# -*- coding: utf-8 -*-
import flickrapi
import requests

import _configFlickr

url = 'https://api.flickr.com/services/rest/'
API_KEY = _configFlickr.api_key

payload = {
    'method': 'flickr.photos.search',
    'api_key': API_KEY,
    'text': 'smile',
    'per_page': '50',
    'format': 'json',
    'nojsoncallback': '1'
    }

r = requests.get(url, params=payload)
flickr = flickrapi.FlickrAPI(_configFlickr.api_key, _configFlickr.api_secret, cache=True)

resp = r.json()
tpl_url = 'https://farm%s.staticflickr.com/%s/%s_%s.jpg'
count = 1
for i in resp['photos']['photo']:
    img_url = tpl_url % (i['farm'],i['server'],i['id'],i['secret'])
    print "#%04d" % count, img_url

    photoLoc = flickr.photos_geo_getLocation(photo_id=i['id'])
    if photoLoc is None:
        continue

    print photoLoc[0][0].attrib['latitude']
    print photoLoc[0][0].attrib['longitude']

    r = requests.get(img_url)
    fname = "%04d.jpg" % count
    f = open(fname, 'wb')
    f.write(r.content)
    f.close()
    count += 1