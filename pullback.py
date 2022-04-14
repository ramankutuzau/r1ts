import backtrader as bt


# Create a Strategy

class Strategy(bt.Strategy):

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
        self.stop_loss = None

        self.profit_count = 0
        self.loss_count = 0

        self.take_profit = None

        self.order_open = None


        self.sma1 = bt.indicators.SMA(period=200)
        self.sma2 = bt.indicators.SMA(period=10)


    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            return
        self.order = None
    def next(self):

        if self.order:
            return

        if not self.position:
            if(self.dataclose[-1] > self.sma1) and (self.dataclose[-1] < self.sma2):
                self.order = self.buy()
                self.stop_loss = self.dataclose / 100 * 98
                self.order_open = self.dataclose[0]
        else:
            if(self.dataopen[0] > self.sma2):
                self.order = self.close()
                self.log('profit : %.2f' % (self.dataclose[0] - self.order_open))
                self.profit_count += 1
            if(self.dataopen[0] <= self.stop_loss):
                self.order = self.close()
                self.log('minus : %.2f' % (self.dataclose[0] - self.order_open))
                self.loss_count += 1
        # print(f'{self.profit_count}/{self.loss_count}')
