import backtrader as bt

from Strategies.Patterns import inside_bar, outside_bar, pin_bar, ppr_bar, uncertainty_bar, uncertainty_uncertainty_bar, \
    takeovers_bar, fake_bar, stars_bar, crows_soldiers_bar, stars_doji_bar,rails_bar,tweezers_bar,\
    dark_veil_bar,capture_belt_bar
import io,os
import datetime

class Strategy(bt.Strategy):

    def __init__(self):
        self.data = []
        self.dataclose = self.datas[0].close
        self.dataopen = self.datas[0].open
        self.datahigh = self.datas[0].high
        self.datalow = self.datas[0].low
        self.count = 0
        # patterns
        self.res_pin = 0
        self.res_inside = 0
        self.res_outside = 0
        self.res_ppr = 0
        self.res_uncertainty = 0
        self.res_uncertainty_uncertainty = 0
        self.res_takeovers = 0
        self.res_fake = 0
        self.res_stars = 0
        self.res_stars_doji = 0
        self.res_crows_soldier = 0
        self.res_rails = 0
        self.res_tweezers = 0
        self.res_dark_veil = 0
        self.res_capture_belt = 0
        # patterns

        self.current_datetime = None
        self.curdtime = None

        # self.pp = bt.indicators.FibonacciPivotPoint(self.data1)
        self.sma_30 = bt.indicators.SMA(period=30)
        # self.sma_200 = bt.indicators.SMA(period=200)


    def next(self):

        self.curdtime = self.datetime.datetime(ago=0)  # 0 is the default

        self.check_patterns_history(variant='history')
        with open('Strategies/timeframe', 'r') as f:
            for timeframe in f:
                pass
                # print(timeframe)

        self.current_datetime = datetime.datetime.now()

        # if ( self.curdtime.strftime(timeframe) == self.current_datetime.strftime('2022-04-08 14:00:00') ):
        self.current_datetime = self.current_datetime - datetime.timedelta(hours=2)
        if ( self.curdtime.strftime(timeframe) == self.current_datetime.strftime("%Y-%m-%d %H:00:00")):
            print('check current')
            self.check_patterns_current(variant='current')

        # self.count += 1
        # print(self.count)

    def check_patterns_history(self,variant):
        one = -1
        two = -2
        three = -3
        self.res_pin = pin_bar.check(open=self.dataopen[one], close=self.dataclose[one], high=self.datahigh[one], low=self.datalow[one],
                                     sma_30=self.sma_30)
        self.save_quotes(self.res_pin,'pin_bar',variant)

        self.res_inside = inside_bar.check(open=self.dataopen[one], close=self.dataclose[one], high=self.datahigh[one],
                         low=self.datalow[one],
                         prev_open=self.dataopen[two], prev_close=self.dataclose[two], prev_high=self.datahigh[two],
                         prev_low=self.datalow[two],sma_30=self.sma_30)
        self.save_quotes(self.res_inside,'inside_bar',variant)

        self.res_outside = outside_bar.check(open=self.dataopen[one], close=self.dataclose[one], high=self.datahigh[one],
                          low=self.datalow[one],
                          prev_open=self.dataopen[two], prev_close=self.dataclose[two], prev_high=self.datahigh[two],
                          prev_low=self.datalow[two])
        self.save_quotes(self.res_outside,'outside_bar',variant)

        self.res_ppr = ppr_bar.check(open=self.dataopen[one], close=self.dataclose[one], high=self.datahigh[one], low=self.datalow[one],
                      prev_open=self.dataopen[two], prev_close=self.dataclose[two], prev_high=self.datahigh[two],
                      prev_low=self.datalow[two])
        self.save_quotes(self.res_ppr,'ppr_bar',variant)

        # self.res_uncertainty = uncertainty_bar.check(open=self.dataopen[one], close=self.dataclose[one], high=self.datahigh[one],
        #                       low=self.datalow[one],
        #                       prev_open=self.dataopen[two], prev_close=self.dataclose[two], prev_high=self.datahigh[two],
        #                       prev_low=self.datalow[two])
        # self.save_history(self.res_uncertainty,'uncertainty_bar')

        self.res_uncertainty_uncertainty = uncertainty_uncertainty_bar.check(open=self.dataopen[one], close=self.dataclose[one], high=self.datahigh[one],
                                          low=self.datalow[one],
                                          prev_open=self.dataopen[two], prev_close=self.dataclose[two],
                                          prev_high=self.datahigh[two],
                                          prev_low=self.datalow[two])
        self.save_quotes(self.res_uncertainty_uncertainty,'uncertainty_2_bar',variant)

        self.res_takeovers = takeovers_bar.check(open=self.dataopen[one], close=self.dataclose[one], high=self.datahigh[one], low=self.datalow[one],
                            prev_open=self.dataopen[two], prev_close=self.dataclose[two], prev_high=self.datahigh[two],
                            prev_low=self.datalow[two])
        self.save_quotes(self.res_takeovers,'takeovers_bar',variant)

        # self.res_fake = fake_bar.check(open=self.dataopen[one], close=self.dataclose[one], high=self.datahigh[one], low=self.datalow[one],
        #                prev_open=self.dataopen[two], prev_close=self.dataclose[two], prev_high=self.datahigh[two],
        #                prev_low=self.datalow[two],
        #                prev2_open=self.dataopen[three], prev2_close=self.dataclose[three], prev2_high=self.datahigh[three],
        #                prev2_low=self.datalow[three])
        self.save_quotes(self.res_fake,'fake_bar',variant)

        self.res_stars = stars_bar.check(open=self.dataopen[one], close=self.dataclose[one], high=self.datahigh[one], low=self.datalow[one],
                        prev_open=self.dataopen[two], prev_close=self.dataclose[two], prev_high=self.datahigh[two],
                        prev_low=self.datalow[two],
                        prev2_open=self.dataopen[three], prev2_close=self.dataclose[three], prev2_high=self.datahigh[three],
                        prev2_low=self.datalow[three])
        self.save_quotes(self.res_stars,'stars_bar',variant)


        self.res_stars_doji = stars_doji_bar.check(open=self.dataopen[one], close=self.dataclose[one], high=self.datahigh[one], low=self.datalow[one],
                             prev_open=self.dataopen[two], prev_close=self.dataclose[two], prev_high=self.datahigh[two],
                             prev_low=self.datalow[two],
                             prev2_open=self.dataopen[three], prev2_close=self.dataclose[three], prev2_high=self.datahigh[three],
                             prev2_low=self.datalow[three])
        self.save_quotes(self.res_stars_doji,'start_doji_bar',variant)


        self.res_crows_soldier = crows_soldiers_bar.check(open=self.dataopen[one], close=self.dataclose[one], high=self.datahigh[one],
                                 low=self.datalow[one],
                                 prev_open=self.dataopen[two], prev_close=self.dataclose[two],
                                 prev_high=self.datahigh[two],
                                 prev_low=self.datalow[two],
                                 prev2_open=self.dataopen[three], prev2_close=self.dataclose[three],
                                 prev2_high=self.datahigh[three],
                                 prev2_low=self.datalow[three])
        self.save_quotes(self.res_crows_soldier,'crows_soldier_bar',variant)


        self.res_rails = rails_bar.check(open=self.dataopen[one], close=self.dataclose[one], high=self.datahigh[one], low=self.datalow[one],
                        prev_open=self.dataopen[two], prev_close=self.dataclose[two], prev_high=self.datahigh[two],
                        prev_low=self.datalow[two])
        self.save_quotes(self.res_rails,'rails_bar',variant)


        self.res_tweezers = tweezers_bar.check(open=self.dataopen[one], close=self.dataclose[one], high=self.datahigh[one], low=self.datalow[one],
                           prev_open=self.dataopen[two], prev_close=self.dataclose[two], prev_high=self.datahigh[two],
                           prev_low=self.datalow[two])
        self.save_quotes(self.res_tweezers,'tweezers_bar',variant)


        self.res_dark_veil = dark_veil_bar.check(open=self.dataopen[one], close=self.dataclose[one], high=self.datahigh[one], low=self.datalow[one],
                            prev_open=self.dataopen[two], prev_close=self.dataclose[two], prev_high=self.datahigh[two],
                            prev_low=self.datalow[two])
        self.save_quotes(self.res_dark_veil,'dark_veil_bar',variant)


        self.res_capture_belt = capture_belt_bar.check(open=self.dataopen[one], close=self.dataclose[one], high=self.datahigh[one], low=self.datalow[one])
        self.save_quotes(self.res_capture_belt,'capture_belt_bar',variant)


    def check_patterns_current(self,variant):
        one = 0
        two = -1
        three = -2
        self.res_pin = pin_bar.check(open=self.dataopen[one], close=self.dataclose[one], high=self.datahigh[one], low=self.datalow[one],
                                     sma_30=self.sma_30)
        self.save_quotes(self.res_pin,'pin_bar',variant)

        self.res_inside = inside_bar.check(open=self.dataopen[one], close=self.dataclose[one], high=self.datahigh[one],
                         low=self.datalow[one],
                         prev_open=self.dataopen[two], prev_close=self.dataclose[two], prev_high=self.datahigh[two],
                         prev_low=self.datalow[two],sma_30=self.sma_30)
        self.save_quotes(self.res_inside,'inside_bar',variant)

        self.res_outside = outside_bar.check(open=self.dataopen[one], close=self.dataclose[one], high=self.datahigh[one],
                          low=self.datalow[one],
                          prev_open=self.dataopen[two], prev_close=self.dataclose[two], prev_high=self.datahigh[two],
                          prev_low=self.datalow[two])
        self.save_quotes(self.res_outside,'outside_bar',variant)

        self.res_ppr = ppr_bar.check(open=self.dataopen[one], close=self.dataclose[one], high=self.datahigh[one], low=self.datalow[one],
                      prev_open=self.dataopen[two], prev_close=self.dataclose[two], prev_high=self.datahigh[two],
                      prev_low=self.datalow[two])
        self.save_quotes(self.res_ppr,'ppr_bar',variant)

        # self.res_uncertainty = uncertainty_bar.check(open=self.dataopen[one], close=self.dataclose[one], high=self.datahigh[one],
        #                       low=self.datalow[one],
        #                       prev_open=self.dataopen[two], prev_close=self.dataclose[two], prev_high=self.datahigh[two],
        #                       prev_low=self.datalow[two])
        # self.save_history(self.res_uncertainty,'uncertainty_bar')

        self.res_uncertainty_uncertainty = uncertainty_uncertainty_bar.check(open=self.dataopen[one], close=self.dataclose[one], high=self.datahigh[one],
                                          low=self.datalow[one],
                                          prev_open=self.dataopen[two], prev_close=self.dataclose[two],
                                          prev_high=self.datahigh[two],
                                          prev_low=self.datalow[two])
        self.save_quotes(self.res_uncertainty_uncertainty,'uncertainty_2_bar',variant)

        self.res_takeovers = takeovers_bar.check(open=self.dataopen[one], close=self.dataclose[one], high=self.datahigh[one], low=self.datalow[one],
                            prev_open=self.dataopen[two], prev_close=self.dataclose[two], prev_high=self.datahigh[two],
                            prev_low=self.datalow[two])
        self.save_quotes(self.res_takeovers,'takeovers_bar',variant)

        # self.res_fake = fake_bar.check(open=self.dataopen[one], close=self.dataclose[one], high=self.datahigh[one], low=self.datalow[one],
        #                prev_open=self.dataopen[two], prev_close=self.dataclose[two], prev_high=self.datahigh[two],
        #                prev_low=self.datalow[two],
        #                prev2_open=self.dataopen[three], prev2_close=self.dataclose[three], prev2_high=self.datahigh[three],
        #                prev2_low=self.datalow[three])
        self.save_quotes(self.res_fake,'fake_bar',variant)

        self.res_stars = stars_bar.check(open=self.dataopen[one], close=self.dataclose[one], high=self.datahigh[one], low=self.datalow[one],
                        prev_open=self.dataopen[two], prev_close=self.dataclose[two], prev_high=self.datahigh[two],
                        prev_low=self.datalow[two],
                        prev2_open=self.dataopen[three], prev2_close=self.dataclose[three], prev2_high=self.datahigh[three],
                        prev2_low=self.datalow[three])
        self.save_quotes(self.res_stars,'stars_bar',variant)


        self.res_stars_doji = stars_doji_bar.check(open=self.dataopen[one], close=self.dataclose[one], high=self.datahigh[one], low=self.datalow[one],
                             prev_open=self.dataopen[two], prev_close=self.dataclose[two], prev_high=self.datahigh[two],
                             prev_low=self.datalow[two],
                             prev2_open=self.dataopen[three], prev2_close=self.dataclose[three], prev2_high=self.datahigh[three],
                             prev2_low=self.datalow[three])
        self.save_quotes(self.res_stars_doji,'start_doji_bar',variant)


        self.res_crows_soldier = crows_soldiers_bar.check(open=self.dataopen[one], close=self.dataclose[one], high=self.datahigh[one],
                                 low=self.datalow[one],
                                 prev_open=self.dataopen[two], prev_close=self.dataclose[two],
                                 prev_high=self.datahigh[two],
                                 prev_low=self.datalow[two],
                                 prev2_open=self.dataopen[three], prev2_close=self.dataclose[three],
                                 prev2_high=self.datahigh[three],
                                 prev2_low=self.datalow[three])
        self.save_quotes(self.res_crows_soldier,'crows_soldier_bar',variant)


        self.res_rails = rails_bar.check(open=self.dataopen[one], close=self.dataclose[one], high=self.datahigh[one], low=self.datalow[one],
                        prev_open=self.dataopen[two], prev_close=self.dataclose[two], prev_high=self.datahigh[two],
                        prev_low=self.datalow[two])
        self.save_quotes(self.res_rails,'rails_bar',variant)


        self.res_tweezers = tweezers_bar.check(open=self.dataopen[one], close=self.dataclose[one], high=self.datahigh[one], low=self.datalow[one],
                           prev_open=self.dataopen[two], prev_close=self.dataclose[two], prev_high=self.datahigh[two],
                           prev_low=self.datalow[two])
        self.save_quotes(self.res_tweezers,'tweezers_bar',variant)


        self.res_dark_veil = dark_veil_bar.check(open=self.dataopen[one], close=self.dataclose[one], high=self.datahigh[one], low=self.datalow[one],
                            prev_open=self.dataopen[two], prev_close=self.dataclose[two], prev_high=self.datahigh[two],
                            prev_low=self.datalow[two])
        self.save_quotes(self.res_dark_veil,'dark_veil_bar',variant)


        self.res_capture_belt = capture_belt_bar.check(open=self.dataopen[one], close=self.dataclose[one], high=self.datahigh[one], low=self.datalow[one])
        self.save_quotes(self.res_capture_belt,'capture_belt_bar',variant)

    def save_quotes(self,result,name,variant):

        if (variant == 'current'):
            file_curr = open(f'current_temp', 'a')
            with io.open('history_temp', encoding='utf-8') as file:
                for line in file:
                    if name in line:
                        str_temp = line.replace(f'{name}:', '')  # deleted bar
                        res = tuple(map(int, str_temp.split(',')))  # convert to tuple

                        log = open(f'logs/logs_forex', 'a')
                        prediction = open(f'logs/prediction_forex', 'a')
                        dataname = self.getdatanames()
                        if (result == 2):
                            log.write(f'\n{dataname[0]} {self.curdtime + datetime.timedelta(hours=2)}\n {name}: SELL statistic: {res[0]}/{res[1]} winrate: {res[2]} \n')
                            prediction.write(f'{dataname[0]}.csv {self.curdtime + datetime.timedelta(hours=2)} sell\n')

                        elif (result == 1):
                            log.write(f'\n{dataname[0]} {self.curdtime + datetime.timedelta(hours=2)}\n {name}: BUY statistic: {res[0]}/{res[1]} winrate: {res[2]} \n')
                            prediction.write(f'{dataname[0]}.csv {self.curdtime + datetime.timedelta(hours=2)} buy\n')

                # prediction.close()
                # log.close()
                # file_curr.close()

        elif(variant == 'history'):

            with io.open('history_temp', encoding='utf-8') as file:
                for line in file:
                    if name in line:  # ищем бар
                        str_temp = line.replace(f'{name}:', '')  # deleted bar
                        res = tuple(map(int, str_temp.split(',')))  # convert to tuple
                        win = res[0]
                        loss = res[1]
                        if (result == 2):
                            if (self.dataclose[0] < self.dataclose[-1]):
                                win += 1
                            else:
                                loss += 1
                        elif (result == 1):
                            if (self.dataclose[0] >= self.dataclose[-1]):
                                win += 1
                            else:
                                loss += 1
                        if not (win == 0) or not (loss == 0):
                            write_str = f'{name}:{win},{loss},{int(win / ((win + loss) / 100))}\n'
                        else:
                            write_str = f'{name}:{win},{loss},0\n'

                        with open('history_temp', 'r') as f:
                            old_data = f.read()
                        new_data = old_data.replace(line, write_str)
                        with open('history_temp', 'w') as f:
                            f.write(new_data)





