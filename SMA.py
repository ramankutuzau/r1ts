import backtrader as bt


# Create a Strategy

class SMAST(bt.Strategy):

    def log(self, txt, dt=None):
        ''' Logging function fot this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self):
        # Keep a reference to the "close" line in the data[0] dataseries
        self.dataclose = self.datas[0].close
        self.dataopen = self.datas[0].open
        self.datahigh = self.datas[0].high

        # To keep track of pending orders
        self.order = None
        self.last_buy = None
        self.r1 = None
        self.s2 = None
        self.profit = None
        self.prev_support = None
        self.min_for_buy = None
        self.prev_resistens = None

        self.high_count = []
        self.stop_lose = None

        self.sma1 = bt.indicators.SMA(period=200)
        self.sma2 = bt.indicators.SMA(period=50)
        # self.sma1.plotinfo.plot = False
        # self.sma2.plotinfo.plot = False
        self.pp = bt.indicators.PivotPoint(self.data1,_autoplot=False)
        self.pp1 = bt.indicators.PivotPoint(self.data2)


    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            # Buy/Sell order submitted/accepted to/by broker - Nothing to do
            return

        # Check if an order has been completed
        # Attention: broker could reject order if not enough cash
        # if order.status in [order.Completed]:
        #     if order.isbuy():
        #         self.log('BUY EXECUTED, %.2f' % order.executed.price)
        #     elif order.issell():
        #         self.log('SELL EXECUTED, %.2f' % order.executed.price)
        #
        #     self.bar_executed = len(self)
        #
        # elif order.status in [order.Canceled, order.Margin, order.Rejected]:
        #     self.log('Order Canceled/Margin/Rejected')

        # Write down: no pending order
        self.order = None

    def next(self):

        if self.order:
            return

        in_middle = (self.dataclose[0] < self.sma1) and (
                    self.dataclose[0] > self.sma2)  # меньше SMA(200) и больше SMA(50)
        if in_middle and len(self.high_count) <= 5:
            self.high_count.append(self.datahigh + 0.0)
        else:
            self.high_count = []

        if not self.position:
            print(self.high_count)
            if (self.dataclose[0] < self.sma2) and (len(self.high_count) > 0):  # return in < SMA(50)
                self.order = self.sell()
                self.profit = self.dataclose[0]
                self.r1 = self.pp1.lines.r1 + 0.0
                self.s2 = self.pp1.lines.s2 + 0.0
                self.stop_lose = max(self.high_count)
            else:
                print(f' sma = {self.sma2 + 0.0} high-count = {len(self.high_count)}')
        else:

            if (self.dataclose[0] >= self.stop_lose):
                self.order = self.close()
                if not (self.r1 == self.pp1.lines.r1):  # next resistens level
                    if (self.dataclose[0] >= self.r1):  # close without profit
                        self.order = self.close()
                        self.log('Close without profit : %.2f' % self.dataclose[0])
                        print(f'profit: {(self.dataclose[0] - self.profit) * - 1}')
                        self.profit = None

                    if (self.dataclose[0] <= self.s2):  # close with profit
                        self.order = self.close()
                        self.log('Close with profit : %.2f' % self.dataclose[0])
                        print(f'profit: {(self.dataclose[0] - self.profit) * - 1}')
                        self.profit = None
