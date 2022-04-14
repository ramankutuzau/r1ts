from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import datetime  # For datetime objects
import os.path  # To manage paths
import sys  # To find out the script name (in argv[0])
import argparse
# Import the backtrader platform
import backtrader as bt
import datetime
import yfinance as yf

import Points_SMA
import SMA
import pullback


def runstrat():
    # Create a cerebro entity
    cerebro = bt.Cerebro()

    # Datas are in a subfolder of the samples. Need to find where the script is
    # because it could have been called from anywhere
    modpath = os.path.dirname(os.path.abspath(sys.argv[0]))
    datapath = os.path.join(modpath, 'USDJPY.csv')
    data = bt.feeds.GenericCSVData(
        dataname=datapath,
        dtformat=('%Y%m%d'),
        tmformat=('%H:%M:%S'),
        datetime=0,
        time=1,
        open=2,
        high=3,
        low=4,
        close=5,
        volume=6,
        timeframe=bt.TimeFrame.Minutes,
        # fromdate=datetime.datetime(2022, 4, 11),
        # todate=datetime.datetime(2022, 4, 13)


    )

    # data = bt.feeds.PandasData(dataname=yf.download('^DJI', '2019-04-13', '2022-04-13'))
    # data = bt.feeds.PandasData(dataname=yf.download('AAPL', '2019-04-13', '2022-04-13'))
    # data = bt.feeds.PandasData(dataname=yf.download('GC=F', '2019-04-13', '2022-04-13'))

    cerebro.adddata(data)

    args = parse_args()

    # cerebro.resampledata(data, timeframe=bt.TimeFrame.Days,compression=1)
    # cerebro.resampledata(data, timeframe=bt.TimeFrame.Minutes,compression=240)
    # cerebro.resampledata(data, timeframe=bt.TimeFrame.Minutes,compression=240)

    cerebro.addstrategy(Points_SMA.Strategy)

    # Set our desired cash start
    cerebro.broker.setcash(1000000000.0)

    # Print out the starting conditions
    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

    # Run over everything
    cerebro.run()
    # Print out the final result
    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
    # cerebro.plot(style='bar')


def parse_args():
    parser = argparse.ArgumentParser(
        description='Pandas test script')
    #
    # parser.add_argument('--dataname', default='', required=False,
    #                     help='File Data to Load')
    #
    # parser.add_argument('--timeframe', default='weekly', required=False,
    #                     choices=['daily', 'weekly', 'monhtly'],
    #                     help='Timeframe to resample to')

    parser.add_argument('--compression', default=1, required=False, type=int,
                        help='Compress n bars into 1')

    return parser.parse_args()



if __name__ == '__main__':
    runstrat()