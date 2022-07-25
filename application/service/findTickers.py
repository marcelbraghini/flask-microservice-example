import yfinance as yf

"""
Find tickers:
target = 'TAEE4F.SA WEGE3F.SA'
"""


def find_tickers(target):
    params = __build_filter(target)

    tickers = yf.Tickers(params)

    actionsList = tickers.tickers
    actions = []

    for a in actionsList:
        info = actionsList[a].info

        action = {
            'action': info['symbol'],
            'lastClose': info['previousClose'],
            'lastPrice': info['regularMarketPrice'],
            'buyValue': info['ask'],
            'sellValue': info['bid']
        }

        actions.append(action)

    return actions


def __build_filter(target):
    params = ''

    for action in target:
        params = params + ' ' + action

    return params.strip()
