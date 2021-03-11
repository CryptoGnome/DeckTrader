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


def create_string():
    # generate random strings for broker order ids
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
    baseId = 'x-40PTWbMI'
    clientId = baseId + str(res)
    return clientId

params = {
    "newClientOrderId": create_string()
}

print("Cancel Orders Called")


openOrders = binance.fapiPrivateGetOpenOrders()
if openOrders:

    for orders in openOrders:
        if orders['symbol'] == symbol + 'USDT':
            binance.cancel_order(orders['orderId'], symbol + '/USDT')










exit()

