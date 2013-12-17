#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import json

def btcticker(field='last'):
    url = 'https://btc-e.com/api/2/btc_usd/ticker'
    data = json.loads(urllib.urlopen(url).read())
    if field in data['ticker'].keys():
        return '[BTC-info] %s:%s' % (field, data['ticker']['last'])
    else:
        return '[BTC-info] last:%s, high:%s, low:%s, buy:%s, sell:%s, volume:%s' % (data['ticker']['last'],data['ticker']['high'],data['ticker']['low'],data['ticker']['buy'],data['ticker']['sell'],data['ticker']['vol'])

