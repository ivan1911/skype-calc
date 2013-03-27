#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Description
***********
Получение траффика в городе
Дополнительно используется модуль "pytils" https://github.com/j2a/pytils/

"""

import urllib2
from xml.dom import minidom
from pytils import numeral


def ytraffic(city_id, result='dict'):
    """ Забираем по XML пробки, город устанавливаем в COOKIE """
    url = 'http://export.yandex.ru/bar/reginfo.xml'
    opener = urllib2.build_opener()
    opener.addheaders.append(('Cookie', 'yandex_gid=' + str(city_id)))
    response = opener.open(url)
    opener.close()
    dom = minidom.parseString(response.read())
    tdata = {}
    for node in dom.getElementsByTagName('traffic'):
        for lnode in node.getElementsByTagName('hint'):
            if lnode.getAttribute('lang') in ['ru', 'en']:
                tdata['hint_' + lnode.getAttribute('lang')] = lnode.firstChild.data
        for k in ['title', 'time', 'level', 'url']:
            tdata[k] = node.getElementsByTagName(k)[0].firstChild.data
    tdata['level_title'] = numeral.choose_plural(int(tdata['level']), (u"балл", u"балл", u"баллов"))
    if result == 'str':
        return u"[ПРОБКИ] %s: %s %s (%s), на %s" % (tdata['title'], tdata['level'], tdata['level_title'], tdata['hint_ru'], tdata['time'])
    return tdata

#print(ytraffic(1, 'str').encode('utf8'))
