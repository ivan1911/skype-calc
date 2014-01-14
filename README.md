# SkypeCALC Bot 
[![GitHub version](https://badge.fury.io/gh/ivan1911%2Fskype-calc.png)](http://badge.fury.io/gh/ivan1911%2Fskype-calc)

## Overview

SkypeCalcBot - Python calc and weather,traffic bot
Developed special for #ganditi

### Commands
```
calc [word] (get calc)

calc [word]=[description] (set calc descriptoin)

cfind [word] (search by calc key start)

mcalc [word] (search by value)

tempmsk, tempspb ... temp(msk|sim|thai|spb|ist|hel|ny|miami|scruz|ant|la)  (weather temp)

probkimsk, probkispb, probki (get traffic info)

btc (get btc currency info)

ltc (get ltc currency info)
```
### Required Python modules

* Skype4py <https://github.com/awahlig/skype4py> (SkypeAPI)
* Python Weather API (pywapi) <https://code.google.com/p/python-weather-api/>
(Yahoo Weather)
* Pytils <https://github.com/j2a/pytils/> (russian word declension)


### calcdata.txt example
```
'dark_fred'||'Zashitnik nervnih detey'||'*'
```
