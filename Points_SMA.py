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
        self.datahigh = self.datas[0].high
        self.datalow = self.datas[0].low

        # To keep track of pending orders
        self.order = None
        self.stop_loss = None

        self.profit_count = 0
        self.loss_count = 0

        self.take_profit = None
        self.profit = None
        self.body = None
        self.shadow_down = None
        self.shadow_down_points = None
        self.shadow_up = None
        self.shadow_up_points = None


        self.order_open = None
        self.count = 0


        # self.sma1 = bt.indicators.SMA(period=200)
        # self.sma2 = bt.indicators.SMA(period=10)


    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            return
        self.order = None
    def next(self):

        if self.order:
            return

        # if (self.dataclose[-1] <= self.dataclose[-2]):
        self.order = self.sell()
        self.profit = self.dataclose[-1] - self.dataopen[-1] # bar +/-
        self.body = round(self.dataclose[-1] / 100 * self.profit,2) # percent in bar
        # print(f'{self.count} open: {self.dataopen[-1]} close {self.dataclose[-1]} profit {self.profit}'
        #       f' percent {self.percent} {round(self.percent,2)}')
        if(self.body > 0.0):
            self.shadow_up_points = self.datahigh[-1] - self.dataclose[-1]
            self.shadow_up = round(self.datahigh[-1] / 100 * self.shadow_up_points,2)
            # print(f'high {self.datahigh[-1]} close {self.dataclose[-1]} per {round(self.shadow_up,2)}')
            self.shadow_down_points = self.dataopen[-1] - self.datalow[-1]
            self.shadow_down = round(self.dataopen[-1] / 100 * self.shadow_down_points,2)
            # print(f'open {self.dataopen[-1]} low {self.datalow[-1]} per {round(self.shadow_down,2)}')

        # self.shadow_up =
        self.count += 1
        print(f'#{self.count} body {self.body} shadow: up({self.shadow_up}) down({self.shadow_down})')
        # if not self.position:
        #     pass
        #     # if (self.dataclose[0] < self.dataclose[-1]):
        #     #     self.order = self.buy()
        # else:
        #     pass
