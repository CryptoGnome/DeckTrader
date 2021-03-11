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
    amt = settings['ladderOrderSize']
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




print("Placing Limit Order")
tickers = order_size()

#calculate offsets
offset = tickers[1] * settings['limitOffset']/100
price = tickers[1] - offset
price2 = tickers[1] - (offset * 32)
price3 = tickers[1] - (offset * 64)
price4 = tickers[1] - (offset * 128)
price5 = tickers[1] - (offset * 256)

#calculate sizing
size = tickers[0]

binance.create_limit_buy_order(symbol + '/USDT', size * 0.025, price, params={"newClientOrderId": create_string()})
binance.create_limit_buy_order(symbol + '/USDT', size * 0.05, price2 , params={"newClientOrderId": create_string()})
binance.create_limit_buy_order(symbol + '/USDT', size * 0.10, price3, params={"newClientOrderId": create_string()})
binance.create_limit_buy_order(symbol + '/USDT', size * 0.30, price4, params={"newClientOrderId": create_string()})
binance.create_limit_buy_order(symbol + '/USDT', size * 0.55, price5, params={"newClientOrderId": create_string()})







exit()

