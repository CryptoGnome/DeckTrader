import json

symbol = 'HNT'



with open('../settings.json', 'r') as fp:
    settings = json.load(fp)

input = {
    'symbol': symbol,
    "leverage": settings['leverage'],
    "limitOffset": settings['limitOffset'],
    "smallOrderSize": settings['smallOrderSize'],
    "largeOrderSize": settings['largeOrderSize'],
    "ladderOrderSize": settings['ladderOrderSize'],
    "limitPartialSize": settings['limitPartialSize'],
    'key': settings['key'],
    'secret': settings['secret']
}
fp.close()

print(json.dumps(input, indent=4))
with open('../settings.json', 'w') as fp:
    json.dump(input, fp, indent=4)

fp.close()

