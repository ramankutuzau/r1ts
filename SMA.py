# Import the backtrader platform
import numpy

import backtrader as bt


# Create a Strategy
class TestStrategy(bt.Strategy):

    def log(self, txt, dt=None):
        ''' Logging function for this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self):
        # Keep a reference to the "close" line in the data[0] dataseries
        self.dataclose = self.datas[0].close
        # self.data = self.data
        # self.dataopen = self.datas[0].open
        self.sma1 = bt.indicators.SMA(period=50)
        self.sma2 = bt.indicators.SMA(period=5)
        # self.pivotindicators = bt.indicators.PivotPoint(self.data)
        # self.pp = bt.indicators.PivotPoint(self.datas[0])

        # self.pp =  bt.indicators.PivotPoint(self.datas[-1])
        # self.pp.plotinfo.plot = True  # activate plotting
        self.pp = bt.indicators.PivotPoint(self.data1)
        #
        # if self.p.multi:
        #     pp1 = pp()  # couple the entire indicators
        #     self.sellsignal = self.data0.close < pp1.s1
        # else:
        #     self.sellsignal = self.data0.close < pp.s1()
    sell = 0.0
    order = None

    def next(self):

        if self.order:
            return

        if not self.position:
            pass
        # Simply log the closing price of the series from the reference
        self.log('Close, %.2f' % self.dataclose[0])
        if self.dataclose < self.sma1 < self.sma2:
            self.order = self.buy()
            self.log('Close, %.2f' % self.dataclose[0])
            self.sell = self.pp.lines.p

        if self.order <= self.sell:
            self.sell()


class SMAST(bt.Strategy):

    def log(self, txt, dt=None):
        ''' Logging function fot this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self):
        # Keep a reference to the "close" line in the data[0] dataseries
        self.dataclose = self.datas[0].close
        self.dataopen = self.datas[0].open

        # To keep track of pending orders
        self.order = None
        self.max = None
        self.min = None
        self.min_for_buy = None
        self.sma1 = bt.indicators.SMA(period=200)
        self.sma2 = bt.indicators.SMA(period=50)
        self.pp = bt.indicators.PivotPoint(self.data1)

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            # Buy/Sell order submitted/accepted to/by broker - Nothing to do
            return

        # Check if an order has been completed
        # Attention: broker could reject order if not enough cash
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log('BUY EXECUTED, %.2f' % order.executed.price)
            elif order.issell():
                self.log('SELL EXECUTED, %.2f' % order.executed.price)

            self.bar_executed = len(self)

        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log('Order Canceled/Margin/Rejected')

        # Write down: no pending order
        self.order = None

    def next(self):
        # Simply log the closing price of the series from the reference
        # self.log('Close, %.2f' % self.dataclose[0])

        # Check if an order is pending ... if yes, we cannot send a 2nd one
        if self.order:
            return
        # self.max = self.pp.lines.r2
        # self.min_for_buy = self.pp.lines.s1
        # Check if we are in the market
        if not self.position:

            # Not yet ... we MIGHT BUY if ...
            if self.dataclose[0] > self.sma2 and self.dataclose[0] < self.sma1:
                # if self.dataclose[0] < self.pp.lines.s1:


                    # r2
                    p = (self.pp.data.high + self.pp.data.low + self.pp.data.close) / 3.0
                    self.max = p + (self.pp.data.high - self.pp.data.low)
                    # print(self.max)
                    # r2
                        # current close less than previous close

                    # BUY, BUY, BUY!!! (with default parameters)

                    # Keep track of the created order to avoid a 2nd order
                    self.order = self.sell()
                    self.log('поставил на продажу, %.2f' % self.dataclose[0])

            # s2
                    p = (self.pp.data.high + self.pp.data.low + self.pp.data.close) / 3.0
                    self.min = p - (self.pp.data.high - self.pp.data.low)
                    print(f' Должен продать меньше = {self.min}')
                    # s2


        else:
            if self.dataclose[0] <= self.min:
                self.log('продал по  %.2f' % self.dataclose[0])
                self.order = self.buy()
                self.min = None

            # if self.dataclose[0] >= self.max:
            #     self.log('SELL CREATE, %.f' % self.dataclose[0])
            #
            #     # Keep track of the created order to avoid a 2nd order
            #     self.order = self.sell()
            #     self.max = None
            # Already in the market ... we might sell
            # if len(self) >= (self.bar_executed + 5):
            #     # SELL, SELL, SELL!!! (with all possible default parameters)
            #     self.log('SELL CREATE, %.2f' % self.dataclose[0])
            #
            #     # Keep track of the created order to avoid a 2nd order
            #     self.order = self.sell()
