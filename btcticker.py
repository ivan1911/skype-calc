#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import json

def btcticker(field='last'):
	if (field == ''):
		field = 'last'
    url = 'https://btc-e.com/api/2/btc_usd/ticker'
    data = json.loads(urllib.urlopen(url).read())
    if field in data['ticker'].keys():
        return '[BTC] %s:%s' % (field, data['ticker']['last'])
    else:
        return '[BTC] field "%s" not found' % (field)

