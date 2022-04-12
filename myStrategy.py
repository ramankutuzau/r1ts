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

        # To keep track of pending orders
        self.order = None
        self.last_buy = None
        self.r1_profit = None
        self.s1_lose = None
        self.prev_support = None
        self.min_for_buy = None

        self.sma1 = bt.indicators.SMA(period=200)
        self.sma2 = bt.indicators.SMA(period=50)
        self.sma1.plotinfo.plot = False
        self.sma2.plotinfo.plot = False
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

        # print(f'data:{self.dataclose[0]} s1 = {self.pp.lines.s1 + 0.0}')
        # Check if an order is pending ... if yes, we cannot send a 2nd one
        if self.order:
            return
        # self.max = self.pp.lines.r2
        # self.min_for_buy = self.pp.lines.s1
        # Check if we are in the market
        if not self.position:

            # TheLupa
            if not (self.prev_support == self.pp.lines.s1 + 0.0):  # 1 сделка на уровень
                # print(f's1={self.pp.lines.s1 + 0.0} r1={self.pp.lines.r1 + 0.0}')
                if (self.dataclose[0] >= self.pp.lines.s1) and (
                        self.dataclose[-1] <= self.pp.lines.s1):  # откскок от уровня поддержки 1 ( 2 бара )
                    # self.r1_profit = self.pp.lines.r1 + 0.0
                    self.s1_lose = self.pp.lines.s1 + 0.0
                    self.r1_profit = self.pp.lines.r1 + 0.0
                    self.order = self.buy()
                    self.log('Купил : %.4f' % self.dataclose[0])
                    self.prev_support = self.pp.lines.s1 + 0.0
                    # # self.log(f'Должен продать >= {self.r1_profit}')
                    # self.last_buy = self.dataclose[0]
                    # print(f'last_buy: {self.las_buy}')
        # TheLupa
        else:  # 1.10 1.0 9
            # TheLupa
            if (self.dataclose[0] <= self.pp.lines.s1):  # если опять падает за уровень - закрываем
                self.order = self.close()
            if (self.dataclose[0] >= self.r1_profit):  # фиксируем профит
                print(f'CLOSE {self.r1_profit} with profit')
                self.order = self.close()
            # TheLupa

