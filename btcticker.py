#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import json

def btcticker(ctype='btc', field='last'):
    url = { 
        "btc": 'https://btc-e.com/api/2/btc_usd/ticker',
        "ltc": 'https://btc-e.com/api/2/ltc_usd/ticker'
    }
    data = json.loads(urllib.urlopen(url[ctype]).read())
    if field in data['ticker'].keys():
        return '[%s-info] %s:%s' % (ctype, field, data['ticker']['last'])
    else:
        return '[%s-info] last:%s, high:%s, low:%s, buy:%s, sell:%s, volume:%s' % (ctype, data['ticker']['last'],data['ticker']['high'],data['ticker']['low'],data['ticker']['buy'],data['ticker']['sell'],data['ticker']['vol'])

