from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import datetime  # For datetime objects
import os.path  # To manage paths
import sys  # To find out the script name (in argv[0])

# Import the backtrader platform
import backtrader as bt
from datetime import datetime
import yfinance as yf

import SMA

if __name__ == '__main__':
    # Create a cerebro entity
    cerebro = bt.Cerebro()

    # Datas are in a subfolder of the samples. Need to find where the script is
    # because it could have been called from anywhere
    modpath = os.path.dirname(os.path.abspath(sys.argv[0]))
    datapath = os.path.join(modpath, 'EURUSD.csv')

    data = bt.feeds.PandasData(dataname=yf.download('GBPNZD=X', '2008-01-01', '2022-01-01'),timeframe=bt.TimeFrame.Days)
    # data = bt.feeds.PandasData(dataname=yf.download('TSLA', '2015-01-01', '2019-01-01'))
    # data = btfeeds.ADataFeed(..., timeframe=bt.TimeFrame.Days)
    # cerebro.adddata(data)

    # Add the Data Feed to Cerebro
    cerebro.adddata(data)
    cerebro.resampledata(data, timeframe=bt.TimeFrame.Months)

    cerebro.addstrategy(SMA.SMAST)

    # Set our desired cash start
    cerebro.broker.setcash(100000.0)

    # Print out the starting conditions
    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

    # Run over everything
    cerebro.run()
    # Print out the final result
    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
    cerebro.plot(style='bar')
