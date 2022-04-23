import requests
from Calculate import converter_data
import os
import sys
import backtrader as bt
import Strategies
from Strategies import all_patterns

def get_info_forex(from_symbol, to_symbol, interval):
    API_KEY = 'QASET7JJD5Y9ND47'

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
    converter_data.csv_converter(f'{filename_new}')

    modpath = os.path.dirname(os.path.abspath(sys.argv[0]))
    datapath = os.path.join(modpath + '/Forex_exchange', f"{filename_new}")
    datapath = os.path.join(modpath + '/Forex_exchange', f"GBP_USD_60_1.csv")

    data = dataFeed(dataname=datapath, timeframe=bt.TimeFrame.Minutes, compression=60)

    all_patterns.create_statistic(data)

    return data

class dataFeed(bt.feeds.GenericCSVData):
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
