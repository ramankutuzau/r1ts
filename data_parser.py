import requests
from Calculate import converter_data
import os
import sys
import backtrader as bt
import Strategies
from Strategies import all_patterns
from Statistics import forex,crypto

def get_info_forex(from_symbol, to_symbol, interval):
    API_KEY = 'J4XBC80BE4NW1LNB'

    url = f"https://www.alphavantage.co/query?" \
          f"function=FX_INTRADAY&" \
          f"from_symbol={from_symbol}&" \
          f"to_symbol={to_symbol}&" \
          f"interval={interval}min&" \
          f"apikey={API_KEY}&" \
          f"datatype=csv&" \
          f"outputsize=full"


    r = requests.get(url)
    filename_new = f'{from_symbol}_{to_symbol}_{interval}.csv'
    open(f"Forex_exchange/{filename_new}", "wb").write(r.content)
    converter_data.csv_converter(filename_new,'Forex')

    modpath = os.path.dirname(os.path.abspath(sys.argv[0]))
    datapath = os.path.join(modpath + '/Forex_exchange', f"{filename_new}")

    data = dataFeed_forex(dataname=datapath, timeframe=bt.TimeFrame.Minutes, compression=60)
    forex.create(data=data,from_symbol=from_symbol,to_symbol=to_symbol,interval=interval)

    return data

class dataFeed_forex(bt.feeds.GenericCSVData):
    params = (
        ('dtformat', '%Y-%m-%d %H:%M:%S'),
        ('datetime', 0),
        ('open', 1),
        ('high', 2),
        ('low', 3),
        ('close', 4),
        ('volume', -1),
        ('openinterest', -1)
    )

def get_info_crypto(symbol):
    API_KEY = 'QASET7JJD5Y9ND47'
    # API_KEY = '7ZXC22A6A7LK4WZS'

    url = f"https://www.alphavantage.co/query?" \
          f"function=DIGITAL_CURRENCY_DAILY&" \
          f"symbol={symbol}&" \
          f"apikey={API_KEY}&" \
          f"datatype=csv&" \
          f"market=USD"

    # url = "https://alpha-vantage.p.rapidapi.com/query"
    #
    # querystring = {"market": "USD", "symbol": "BTC", "function": "DIGITAL_CURRENCY_DAILY",'datatype':'csv'}
    #
    # headers = {
    #     "X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com",
    #     "X-RapidAPI-Key": "02e306b399msh0da767285afe408p1b2252jsn248b36027669"
    # }

    # response = requests.request("GET", url, headers=headers, params=querystring)

    # print(response.text)

    r = requests.get(url)
    filename_new = f'{symbol}.csv'
    open(f"Crypto_exchange/{filename_new}", "wb").write(r.content)
    converter_data.csv_converter(filename_new,'Crypto')

    modpath = os.path.dirname(os.path.abspath(sys.argv[0]))
    datapath = os.path.join(modpath + '/Crypto_exchange', f"{filename_new}")

    data = dataFeed_crypto(dataname=datapath, timeframe=bt.TimeFrame.Minutes, compression=60)
    crypto.create(data=data,symbol=symbol)

    return data



class dataFeed_crypto(bt.feeds.GenericCSVData):
    params = (
        ('dtformat', '%Y-%m-%d'),
        ('datetime', 0),
        ('open', 1),
        ('high', 2),
        ('low', 3),
        ('close', 4),
        ('open', 5),
        ('high', 6),
        ('low', 7),
        ('close', 8),
        ('volume', 9),
        ('openinterest', -1)
    )
