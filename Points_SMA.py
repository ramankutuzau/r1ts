import math

import backtrader as bt
from math import floor
# Create a Strategy
import Data
import Prediction_3body_sma
import Prediction_SMA
class Strategy(bt.Strategy,Prediction_SMA.Strategy_SMA):


    def log(self, txt, dt=None):

        ''' Logging function fot this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self):
        self.data = []
        # Keep a reference to the "close" line in the data[0] dataseries
        self.dataclose = self.datas[0].close
        self.dataopen = self.datas[0].open
        self.datahigh = self.datas[0].high
        self.datalow = self.datas[0].low
        # To keep track of pending orders
        self.order = None

        self.shadow_up = None
        self.shadow_down = None
        self.shadow_up = None
        self.shadow_up_points = None

        self.prev_body_per = None # bar +/-
        self.curr_body_per = None # bar +/-

        self.prev_body_point = None
        self.curr_body_point = None


        self.win = 0
        self.loss = 0
        self.count = 0
        self.count_buy = 0
        self.count_sell = 0
        self.winloss = None
        self.result = 0
        self.cash = 10


        self.sma = bt.indicators.SMA(period=50)
        self.sma2 = bt.indicators.SMA(period=200)


    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            return
        self.order = None

    def next(self):

        if self.order:
            return
        self.count += 1
        print(f'count: {self.count}')
        # profit = self.dataclose[-1] - self.dataopen[-1]
        # print(f'proft: {profit}')
        # if (self.dataclose[-1] <= self.dataclose[-2]):
        # self.order = self.sell()
        # profit =  # bar +/-
        # previous_body = self.dataclose[-1] / 100 * profit # percent in previous bar
        # print(self.body)
        # profit = self.dataclose[0] - self.dataopen[0]  # bar +/-
        # current_body = self.dataclose[0] / 100 * profit  # percent in current bar

        # self.calculate_shadows()
        # # self.calculate_bar(bar=bar,type='percent')
        # bar2 = (self.dataopen[-3],self.dataclose[-3],self.datahigh[-3],self.datalow[-3])
        # bar2 = self.calculate_bar(bar=bar2,type='percent',sma1=self.sma[-2])
        # # print(bar2)

        # bar3 = (self.dataopen[-3], self.dataclose[-3], self.datahigh[-3], self.datalow[-3])
        # bar3 = self.calculate_bar(bar=bar3, type='percent',sma1=self.sma[-3])
        # # print(f'bar1 {bar1})')
        #
        #
        # bar2 = (self.dataopen[-2], self.dataclose[-2], self.datahigh[-2], self.datalow[-2],self.sma[-2])
        # bar2 = self.calculate_bar(bar=bar2, type='percent',sma1=self.sma[-2])

        bar2 = (self.dataopen[-2], self.dataclose[-2], self.datahigh[-2], self.datalow[-2],self.sma[-2])
        bar2 = self.calculate_bar(bar=bar2, type='percent',sma1=self.sma[0],sma2=self.sma2[-2])

        bar1 = (self.dataopen[-1], self.dataclose[-1], self.datahigh[-1], self.datalow[-1], self.sma[-1])
        bar1 = self.calculate_bar(bar=bar1, type='percent', sma1=self.sma[-1],sma2=self.sma2[-1])

        bar = (self.dataopen[0], self.dataclose[0], self.datahigh[0], self.datalow[0],self.sma[0])
        bar = self.calculate_bar(bar=bar, type='percent',sma1=self.sma[0],sma2=self.sma2[0])

        self.data_collection(prev_bar=bar2,current_bar=bar1,result_bar=bar)
        # Prediction_3body_sma.Strategy_SMA.check_one_bar(self,prev_bar=bar2, current_bar=bar1,result_bar=bar)
        if (len(self.datas[0]) == 367298):    # КОЛХОЗ
            Data.Processes(data=self.data)

            # self.data_collection(body=prev_body_point, sma=1, next=curr_body_point)
        # prev_body_per = self.to_percent(data_up=self.dataclose[-1], data_down=self.dataopen[-1]) # bar +/-
        # curr_body_per = self.to_percent(data_up=self.dataclose[0], data_down=self.dataopen[0]) # bar +/-
        #
        # prev_body_point = self.body_in_points(dataclose=self.dataclose[-1], dataopen=self.dataopen[-1])
        # curr_body_point = self.body_in_points(dataclose=self.dataclose[0], dataopen=self.dataopen[0])
        #
        # shadow_up = 0.0
        # shadow_down = 0.0

        # self.add_body()

        # if (self.dataclose[-1] >= self.sma):
        #     result = Prediction_SMA.Strategy_SMA.check_one_bar(search=prev_body_point,up=shadow_up,down=shadow_down,sma=1,next=curr_body_per)
        # else:
        #     result = Prediction_SMA.Strategy_SMA.check_one_bar(search=prev_body_point,up=shadow_up,down=shadow_down,sma=0,next=curr_body_per)


        # OPEN POSITION





            # print(f'open: {self.dataopen[-1]} close: {self.dataclose[-1]}')
            # print(shadow_up)
            # print(shadow_down)
        # current_body = self.rounding_body(body=current_body)
        # print(prev_body_point)
        # prev_shadow_up = 0
        # prev_shadow_down = 0
        # if(prev_body_point > 0.0): # if BULL
        #     prev_shadow_up = self.shadow_in_points(x=self.datahigh[-1], y=self.dataclose[-1]) # Upper shadow BULL
        #     prev_shadow_down = self.shadow_in_points(x=self.dataopen[-1], y=self.datalow[-1]) # Down shadow BULL
        # else:
        #     prev_shadow_up = self.shadow_in_points(x=self.datahigh[-1], y=self.dataopen[-1]) # Down shadow for BEAR
        #     prev_shadow_down = self.shadow_in_points(x=self.dataclose[-1], y=self.datalow[-1]) # Down shadow for BEAR

        # in collection
        # if (self.dataclose[-1] >= self.sma): # add SMA(30)
        #     self.data_collection(body=prev_body_point, sma=1, next=curr_body_point)
        # else:
        #     self.data_collection(body=prev_body_point, sma=0, next=curr_body_point)
        # print(prev_body_per)

        # shadow_up_points = self.shadow_in_points(body=prev_body_point,
        #                                        low=self.datalow[-1],
        #                                        high=self.datahigh[-1],
        #                                        close=self.dataclose[-1],
        #                                        open=self.dataopen[-1])
        #
        # shadow_down_points = self.shadow_in_points(body=prev_body_point,
        #                                          low=self.datalow[-1],
        #                                          high=self.datahigh[-1],
        #                                          close=self.dataclose[-1],
        #                                          open=self.dataopen[-1])

        # if (prev_body_point > 0.0):  # SHADOWS in percent
        #     shadow_up_points = self.datahigh[-1] - self.dataclose[-1]
        #     shadow_up = round(self.datahigh[-1] / 100 * shadow_up_points, 2)
        #     # print(f'high {self.datahigh[-1]} close {self.dataclose[-1]} per {round(self.shadow_up,2)}')
        #     shadow_down_points = self.dataopen[-1] - self.datalow[-1]
        #     shadow_down = round(self.dataopen[-1] / 100 * shadow_down_points, 2) * -1

        # if ()

        # print(round(previous_body,5))
        # print(round(current_body,5))
            # self.body = round(self.body,2)
            # print(f'DOBAVIL : {self.body}')
            # self.body += 0.01
            # print(round(self.body,2))
            # print(f'stalo: {self.body}')
            # self.body = round(self.body,2)
            # print(f'output: {self.body}')
            # print(f"было {self.body}")
            # print(f'стало {self.body}')
        # elif (self.body == -0.0):
        #     print(f"было {self.body}")
        #     self.body -= -0.1
        #     print(f'стало {self.body}')
        # print(f'{self.count} open: {self.dataopen[-1]} close {self.dataclose[-1]} profit {self.   profit}'
        #       f' percent {self.percent} {round(self.percent,2)}')

        # print(round(self.body,2))

            # print(f'open {self.dataopen[-1]} low {self.datalow[-1]} per {round(self.shadow_down,2)}')
        # print(self.shadow_down)
        # self.shadow_up =
        # if (self.body == 0.0):
        #     self.buy()
            # print(self.body)
        # self.count += 1
        # print(f'#{self.count} body {self.body} shadow: up({self.shadow_up}) down({self.shadow_down})')
        # if not self.position:
        #     pass
        #     # if (self.dataclose[0] < self.dataclose[-1]):
        #     #     self.order = self.buy()
        # else:
        #     pass
        # previous_body = round(previous_body,6)
        # current_body = round(current_body,6)
        # self.data_collection(body=previous_body,up=shadow_up,down=shadow_down,
        #                      next=current_body)
        # print(len(self.data.buflen()))
        # # if (len(self.datas[0]) == 10000): # КОЛХОЗ
        #     Prediction.Strategy(self.data)
            # Data.Processes(self.data)
            # Data.Processes(self.data)
            # Prediction.Strategy.runstrat()
            # pass
            # print(f'hui {self.data}')
            # Prediction.Strategy.runstrat(data=self.data)
            # Prediction.Strategy.data_collection(self.data)

    def to_points(self,dataclose,dataopen):
        points = dataclose - dataopen
        return int(points * 100000)

    # def shadow_up_points(self,body,high,close,low,open):
    #     if (body > 0.0):  # SHADOWS in percent
    #         points = high - close
    #         # shadow_up = round(high / 100 * points, 2)
    #         # print(f'high {self.datahigh[-1]} close {self.dataclose[-1]} per {round(self.shadow_up,2)}')
    #     else:
    #         points = open - low
    #         # shadow_down = round(self.dataopen[-1] / 100 * shadow_down_points, 2) * -1
    #     return int(points * 100000)

    def shadow_in_points(self,x,y):
        points = x - y
        return int(points * 100000)

    # def shadow_in_percent(self,body,high,close,low,open): # SHADOWS in percent
    #     if (body > 0.0):
    #         points = high - close
    #         shadow = high / 100 * points
    #         print(f'high {self.datahigh[-1]} close {self.dataclose[-1]} per {round(self.shadow_up,2)}')
    #     else:
    #         points = open - low
    #         shadow = (open / 100 * points) * -1
    #     return round(shadow,2)

    def to_percent(self,data_up,data_down):

        # if(dataclose > dataopen):
            # print(f'close {dataclose} open {dataopen}')
            # print(f'open: {dataopen} close {dataclose}')
        difference = data_up - data_down
        percent = round(round(difference * 10000) / 100,2)
            # print(f'raznica {difference}')
            # print(f'raznica in percent {}')
        # else:
        #     difference = dataopen - dataclose
        #     body = round(difference * 1000) / 100 * -1
        #     print(body)

            # print(f'raznica in percent {(round(difference * 1000) / 100) * -1}')
        # body = self.rounding_body(body=body)
        # print(f'dif: {difference}')
        return percent


    # def rounding_body(self, body):
    #     # print(body)
    #     if (body > 0.000001) and (body < 0.009) or (body < -0.000001) and (body > -0.009):  # if < 0.01% add points to 0.01%
    #         add_to_per = 0.01 - body
    #         # print(f'dobavit {self.add_to_per}')
    #         body += add_to_per
    #         # print(body)
    #     # print(f'стало {body}')
    #     return body
    def data_collection(self,prev_bar,current_bar,result_bar):
        # print(f'{self.data} bar {}')
        self.data.append((prev_bar,current_bar,result_bar))
        # print(self.data)
        # Prediction.Test.runstrat()
        # print(self.data)
        # self.count += 1
        # print(self.count)

    def calculate_bar(self,bar,type,sma1,sma2):
        dataopen = bar[0]
        dataclose = bar[1]
        datahigh = bar[2]
        datalow = bar[3]
        sma_1 = sma1
        sma_2 = sma2
        # print(f'SMA {sma}')
        if (type == 'percent'):
            body = self.to_percent(data_up=dataclose, data_down=dataopen)  # bar +/-
            shadows = self.calculate_shadows(body=body,dataopen=dataopen,dataclose=dataclose,
                                             datahigh=datahigh,datalow=datalow)
            if(dataclose >= sma_1):
                sma_1 = 1
            else:
                sma_1 = 0
            if (dataclose >= sma_2):
                sma_2 = 1
            else:
                sma_2 = 0


        elif(type == 'points'):
            body = self.to_points(dataclose=dataclose, dataopen=dataopen)  # bar +/-
            shadows = self.calculate_shadows(body=body,dataopen=dataopen,dataclose=dataclose,
                                             datahigh=datahigh,datalow=datalow)
            # print(f'body {body}')

        bar = (body,shadows[0],shadows[1],sma_1,sma_2)
        return bar

    def calculate_shadows(self,body,dataopen,dataclose,datahigh,datalow):
        up = 0.0
        down = 0.0
        if (body > 0.0):
            up = self.to_percent(datahigh,dataclose)
            down = self.to_percent(dataopen,datalow) * -1
        elif(body < 0.0):
            up = self.to_percent(datahigh,dataopen)
            down = self.to_percent(dataclose,datalow) * -1
        elif(body == 0.0):
            up = self.to_percent(datahigh,dataclose)
            down = self.to_percent(dataopen,datalow) * -1

        return (up,down)

