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
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
    baseId = 'x-40PTWbMI'
    clientId = baseId + str(res)
    return clientId

def order_size():
    amt = settings['largeOrderSize']
    account = binance.fapiPrivateGetAccount()
    balance = round(float(account['totalWalletBalance']), 2)
    tickerDump = binance.fetch_ticker(symbol + '/USDT')
    qtycalc = (balance / tickerDump['last']) * (float(amt) / 100)
    qty = round(qtycalc * int(settings['leverage']), 4)
    return qty




params = {
    "newClientOrderId": create_string()
}
print("Placing Marker Order")

size = order_size()
binance.create_market_buy_order(symbol + '/USDT', size, params)











exit()

