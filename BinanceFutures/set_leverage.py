import ccxt
import json
import string
import random

with open('settings.json', 'r') as fp:
    settings = json.load(fp)
fp.close()

exchange_id = 'binance'
exchange_class = getattr(ccxt, exchange_id)
binance = exchange_class({
    'apiKey': settings['key'],
    'secret': settings['secret'],
    'timeout': 30000,
    'enableRateLimit': True,
    'options': {'defaultType': 'future'},
})


symbol = settings['symbol']


def set_leverage():
    print("Setting Leverage", symbol)
    params = {
        'symbol': symbol + 'USDT',
        'leverage': int(settings['leverage']),
    }
    binance.fapiPrivatePostLeverage(params=params)


set_leverage()
exit()

