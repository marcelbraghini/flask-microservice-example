import yfinance as yf

"""
Find one ticker:
target = 'TAEE4F.SA'
"""


def find_ticker(target):
    data = yf.Ticker(target)
    info = data.info

    action = {
        'action': info['symbol'],
        'lastClose': info['previousClose'],
        'lastPrice': info['regularMarketPrice'],
        'buyValue': info['ask'],
        'sellValue': info['bid']
    }

    return action
