import backtrader as bt
from patterns import inside_bar, outside_bar, pin_bar, ppr_bar, uncertainty_bar, uncertainty_uncertainty_bar, \
    takeovers_bar, fake_bar, stars_bar, crows_soldiers_bar


class Strategies(bt.Strategy):

    def log(self, txt, dt=None):

        ''' Logging function fot this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self):
        self.data = []

        self.dataclose = self.datas[0].close
        self.dataopen = self.datas[0].open
        self.datahigh = self.datas[0].high
        self.datalow = self.datas[0].low

        self.order = None

        self.count = 0

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            return
        self.order = None

    def next(self):
        if self.order:
            return
        # self.count += 1
        # print(self.count)
        pin_bar.check(open=self.dataopen[0], close=self.dataclose[0], high=self.datahigh[0], low=self.datalow[0])

        inside_bar.check(open=self.dataopen[0], close=self.dataclose[0], high=self.datahigh[0],
                               low=self.datalow[0],
                               prev_open=self.dataopen[-1], prev_close=self.dataclose[-1], prev_high=self.datahigh[-1],
                               prev_low=self.datalow[-1])

        outside_bar.check(open=self.dataopen[0], close=self.dataclose[0], high=self.datahigh[0],
                                low=self.datalow[0],
                                prev_open=self.dataopen[-1], prev_close=self.dataclose[-1], prev_high=self.datahigh[-1],
                                prev_low=self.datalow[-1])

        ppr_bar.check(open=self.dataopen[0], close=self.dataclose[0], high=self.datahigh[0], low=self.datalow[0],
                      prev_open=self.dataopen[-1], prev_close=self.dataclose[-1], prev_high=self.datahigh[-1],
                      prev_low=self.datalow[-1])

        uncertainty_bar.check(open=self.dataopen[0], close=self.dataclose[0], high=self.datahigh[0],
                              low=self.datalow[0],
                              prev_open=self.dataopen[-1], prev_close=self.dataclose[-1], prev_high=self.datahigh[-1],
                              prev_low=self.datalow[-1])

        uncertainty_uncertainty_bar.check(open=self.dataopen[0], close=self.dataclose[0], high=self.datahigh[0],
                                          low=self.datalow[0],
                                          prev_open=self.dataopen[-1], prev_close=self.dataclose[-1],
                                          prev_high=self.datahigh[-1],
                                          prev_low=self.datalow[-1])

        takeovers_bar.check(open=self.dataopen[0], close=self.dataclose[0], high=self.datahigh[0], low=self.datalow[0],
                            prev_open=self.dataopen[-1], prev_close=self.dataclose[-1], prev_high=self.datahigh[-1],
                            prev_low=self.datalow[-1])

        fake_bar.check(open=self.dataopen[0], close=self.dataclose[0], high=self.datahigh[0], low=self.datalow[0],
                       prev_open=self.dataopen[-1], prev_close=self.dataclose[-1], prev_high=self.datahigh[-1],
                       prev_low=self.datalow[-1],
                       prev2_open=self.dataopen[-2], prev2_close=self.dataclose[-2], prev2_high=self.datahigh[-2],
                       prev2_low=self.datalow[-2])

        stars_bar.check(open=self.dataopen[0], close=self.dataclose[0], high=self.datahigh[0], low=self.datalow[0],
                        prev_open=self.dataopen[-1], prev_close=self.dataclose[-1], prev_high=self.datahigh[-1],
                        prev_low=self.datalow[-1],
                        prev2_open=self.dataopen[-2], prev2_close=self.dataclose[-2], prev2_high=self.datahigh[-2],
                        prev2_low=self.datalow[-2])

        crows_soldiers_bar.check(open=self.dataopen[0], close=self.dataclose[0], high=self.datahigh[0],
                                 low=self.datalow[0],
                                 prev_open=self.dataopen[-1], prev_close=self.dataclose[-1],
                                 prev_high=self.datahigh[-1],
                                 prev_low=self.datalow[-1],
                                 prev2_open=self.dataopen[-2], prev2_close=self.dataclose[-2],
                                 prev2_high=self.datahigh[-2],
                                 prev2_low=self.datalow[-2])
