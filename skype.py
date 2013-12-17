#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Skype4Py
import time
import re
import pywapi
import codecs
import random
from btcticker import btcticker
from ytraffic import ytraffic
from yweather import yweather
"""
SkypeCalcBot -- calc and weather,traffic bot
Developed special for #ganditi @ skype conferenece

Сommands    calc <word>
========    calc <word>=<descriptiom>
            tempmsk, tempspb, tempsim, temphel, tempist, tempthai
            probkimsk, probkispb
Author
======
ivan.kiselev@gmail.com

Require:
========
Skype4py https://github.com/awahlig/skype4py (SkypeAPI)
Python Weather API (pywapi) https://code.google.com/p/python-weather-api/ (погода Yahoo)
Pytils https://github.com/j2a/pytils/ (склонение русских слов)
"""


class SkypeBot(object):
    def __init__(self):
        self.chatname = 'CHAN NAME CHANGE ME BEFORE STARTUP' # название канала, можно узнать используя skype_chanlist.py
        self.calc_file = 'calcdata.txt' # файл с калками
        self.bot_name = 'SkypeCalcBot' # название бота

        self.skype = Skype4Py.Skype(Events=self)
        self.skype.FriendlyName = self.bot_name
        self.skype.Attach()
        self.calc_dict = {}
        self.LoadCalcDict()
        self.EventFrom = ''

    def LoadCalcDict(self):
        for line in codecs.open(self.calc_file, 'r', encoding='utf8'):
            calc_data = line.split('||')
            self.calc_dict[calc_data[0].replace('\'', '')] = [calc_data[1].replace('\'', ''), calc_data[2].replace('\'', '').rstrip()]

    def AttachmentStatus(self, status):
        if status == Skype4Py.apiAttachAvailable:
            self.skype.Attach()

    def MessageStatus(self, msg, status):

        if (status == Skype4Py.cmsReceived or status == Skype4Py.cmsSent) and msg.Chat.Name == self.chatname:
            for regexp, target in self.commands.items():
                match = re.match(regexp, msg.Body, re.IGNORECASE)
                if match:
                    self.EventFrom = msg.FromHandle
                    reply = target(self, *match.groups())
                    if reply:
                        msg.Chat.SendMessage(reply.encode('utf8'))
                    break

    def cmd_calc(self, calc):
        if calc == '':
            calc = random.choice(self.calc_dict.keys())
        if calc in self.calc_dict:
            return "[ %s = %s added by <%s>]" % (calc, self.calc_dict[calc][0], self.calc_dict[calc][1])
        else:
            return u"%s, no calc found" % self.EventFrom

    def cmd_savecalc(self, calc, calc_body):
        added_by = self.EventFrom
        if calc and calc_body:
            self.calc_dict[calc] = [calc_body, added_by]
            calc_file = codecs.open(self.calc_file, 'a', encoding='utf8')
            calc_file.write("'%s'||'%s'||'%s'\n" % (calc, calc_body, added_by))
            calc_file.close()
            return "thanks for adding <%s>" % added_by

    def cmd_find_calc(self, calc):
        # поиск единичного калка
        find_result = []
        for key, value in self.calc_dict.iteritems():   # iter on both keys and values
            if key.startswith(calc):
                find_result.append(key)
        if len(find_result) > 0:
            top_calc = find_result[0:11]
            return u"Found %s calc for '%s', some of them: %s" % (len(find_result), calc, ', '.join(top_calc))
        else:
            return u"No calc found for '%s'" % calc

    def cmd_find_mcalc(self, calc):
        # поиск по калкам
        find_result = []
        for key, value in self.calc_dict.items():   # iter on both keys and values
            if calc in value[0]:
                find_result.append(key)
        if len(find_result) > 0:
            top_calc = find_result[0:21]
            return u"Found %s calc for '%s', some of them: %s" % (len(find_result), calc, ', '.join(top_calc))
        else:
            return u"No calc found for '%s'" % calc

    def cmd_temp(self, city):
        # погода Яндекс в городах
        city_code = {'msk': '27612', 'spb': '26063', 'ist': '17060', 'sim': '33946', 'hel': '2974', 'thai': '48461', 'ny': '72503', 'miami': '72202', 'scruz': '60020', 'ant': '89050', 'la': '72295'}
        return yweather(city_code[city], 'str')

    def cmd_trafficmsk(self):
        # пробки MSK
        return ytraffic(1, 'str')

    def cmd_trafficspb(self):
        # пробки SPB
        return ytraffic(2, 'str')

    def cmd_btc(self, field):
        # курс btc
        return btcticker(field)
        
    def get_weather(self, city_code):
        # погода Yagoo
        weather = pywapi.get_weather_from_yahoo(city_code)
        return '%s temperature: %sC, %s' % (weather['condition']['title'], weather['condition']['temp'], weather['condition']['text'])

    commands = {
        "!?calc *([^\=]*)$": cmd_calc,
        "!?cfind *(.{3,})$": cmd_find_calc,
        "!?btc *([^\=]*)$": cmd_btc,
        "!?mcalc *(.{3,})$": cmd_find_mcalc,
        "!?calc *([^ ]*) *= *(.*)": cmd_savecalc,
        "^temp(msk|sim|thai|spb|ist|hel|ny|miami|scruz|ant|la)$": cmd_temp,
        "^!?probkimsk|!?probki$": cmd_trafficmsk,
        "^!?probkispb$": cmd_trafficspb
    }

if __name__ == "__main__":

    bot = SkypeBot()

    while True:
        time.sleep(2.0)