#!/usr/bin/python3
# -*- coding:utf-8 -*-

# File Name: fetch_xml.py
# Author: Lipsum
# Mail: niuleipeng@gmail.com
# Created Time: 2016-05-16 15:59:21

from urllib import request, parse

req = request.Request('http://weather.yahooapis.com/forecastrss?u=c&w=2151330')
req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36'
)

with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k,v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))

