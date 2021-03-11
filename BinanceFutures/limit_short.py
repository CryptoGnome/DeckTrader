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


def order_size():
    amt = settings['smallOrderSize']
    account = binance.fapiPrivateGetAccount()
    balance = round(float(account['totalWalletBalance']), 2)
    tickerDump = binance.fetch_ticker(symbol + '/USDT')
    qtycalc = (balance / tickerDump['last']) * (float(amt) / 100)
    qty = round(qtycalc * int(settings['leverage']), 4)
    last = tickerDump['last']
    return qty, last

def create_string():
    # generate random strings for broker order ids
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
    baseId = 'x-40PTWbMI'
    clientId = baseId + str(res)
    return clientId



params = {
    "newClientOrderId": create_string()
}
print("Placing Limit Order")
tickers = order_size()
offset = tickers[1] * settings['limitOffset']/100
price = tickers[1] + offset
binance.create_limit_sell_order(symbol + '/USDT', tickers[0], price, params)











exit()

