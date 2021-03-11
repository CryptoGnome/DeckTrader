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


def create_string():
    # generate random strings for broker order ids
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
    baseId = 'x-40PTWbMI'
    clientId = baseId + str(res)
    return clientId

params = {
    "newClientOrderId": create_string(),
    "reduceOnly": "true"
}

print('Closing Position at Market')


symbol = settings['symbol']



open_positions = binance.fapiPrivateGetPositionRisk()
for position in open_positions:
    if position['symbol'] == symbol + 'USDT':

        if float(position['positionAmt']) > 0:
            size = float(position['positionAmt'])
            binance.create_market_sell_order(symbol + '/USDT', abs(size), params)

        elif float(position['positionAmt']) < 0:
            size = float(position['positionAmt'])

            binance.create_market_buy_order(symbol + '/USDT', abs(size), params)
        else:
            pass





exit()