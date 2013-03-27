#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import time
from xml.dom import minidom

MOSCOW_CITY_ID = 27612


def yweather(city_id, result='dict'):
    url = 'http://export.yandex.ru/weather-ng/forecasts/%s.xml' % city_id

    dom = minidom.parse(urllib.urlopen(url))
    wdata = {}
    # коллектим все атрибуты города
    for node in dom.getElementsByTagName('forecast'):
        for atrname, atrvalue in node.attributes.items():
            wdata[atrname] = atrvalue
    # коллектим все параметры текущей погоды
    for node in dom.getElementsByTagName('fact'):
        wdata['time'] = time.strftime("%Y-%m-%d %H:%M", time.strptime(node.getElementsByTagName('observation_time')[0].firstChild.data[:19], "%Y-%m-%dT%H:%M:%S"))
        wdata['weather_type'] = node.getElementsByTagName('weather_type')[0].firstChild.data
        wdata['temperature'] = node.getElementsByTagName('temperature')[0].firstChild.data
        wdata['wind_speed'] = node.getElementsByTagName('wind_speed')[0].firstChild.data
    # макс и мин значения погоды за текущий день
    for node in dom.getElementsByTagName('informer'):
        # добавляем массив с информаерами по погоде
        wdata['temperature_informer'] = []
        for t in node.getElementsByTagName('temperature'):
            wdata['temperature_informer'].append({'temprature': t.firstChild.data, 'type': t.getAttribute('type')})
    if result == 'str':
        return u'[Погода %s] %sC, %s, ветер %s м/с на %s' % (wdata['exactname'], wdata['temperature'], wdata['weather_type'], wdata['wind_speed'], wdata['time'])
    # забираем информацию по прогнозе на следующие дни (отдельно для утро, день, вечер, ночь)
    wdata['future_temp'] = []
    for node_day in dom.getElementsByTagName('day'):
        node_day.getAttribute('date')
        day_data = {'date': node_day.getAttribute('date'), 'day_part_temprature': []}
        for node_part in node_day.getElementsByTagName('day_part'):
            part_data = {'type': node_part.getAttribute('type'), 'weather_type': node_part.getElementsByTagName('weather_type')[0].firstChild.data}
            if node_part.getElementsByTagName('temperature_from'):
                part_data['temperature_from'] = node_part.getElementsByTagName('temperature_from')[0].firstChild.data
                part_data['temperature_to'] = node_part.getElementsByTagName('temperature_to')[0].firstChild.data
            else:
                part_data['temperature'] = node_part.getElementsByTagName('temperature')[0].firstChild.data
            day_data['day_part_temprature'].append(part_data)
        wdata['future_temp'].append(day_data)
    return wdata

# print(yweather(MOSCOW_CITY_ID, 'str').encode('utf8'))
