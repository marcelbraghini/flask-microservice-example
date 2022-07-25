import yfinance as yf

"""
Find one ticker:
target = { 
    "actionName": "TAEE4F.SA",
    "startDate": "2022-01-01",
    "endDate": "2022-07-30"
}
"""


def find_history_by_ticker(target):
    data = yf.Ticker(target['actionName'])

    history = data.history(start=target['startDate'], end=target['endDate'])

    result = history.to_dict(orient='index')

    return result
