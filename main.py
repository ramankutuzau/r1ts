from __future__ import (absolute_import, division, print_function,
                        unicode_literals)


import os.path  # To manage paths
import sys  # To find out the script name (in argv[0])
import argparse
import backtrader as bt
# from Strategies import all_patterns
import requests
import data_parser
import io
import bot
from time import sleep
from Calculate import converter_data


from datetime import datetime
def runstrat():

    cerebro = bt.Cerebro()
    # check_prediction_forex()
    # data = data_parser.get_info_forex(from_symbol='USD',to_symbol='CHF',interval=60)

    # data = data_parser.get_info_crypto(symbol='BHC')
    # cerebro.adddata(data)
    # current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # print(f'{current_datetime}')
    # str_ = current_datetime

    datetime1 = datetime.now()
    while True:
        # curdtime = datetime.now()
        # if (curdtime.strftime("%Y-%m-%d %H:%M:%S") == datetime1.strftime("%Y-%m-%d %H:00:01")):
        #     print(f'{curdtime.strftime("%Y-%m-%d %H:%M:%S")}')
        print(datetime1)
        data = data_parser.get_info_forex(from_symbol='AUD',to_symbol='CAD',interval=60)
        data = data_parser.get_info_forex(from_symbol='AUD',to_symbol='NZD',interval=60)
        data = data_parser.get_info_forex(from_symbol='EUR',to_symbol='AUD',interval=60)
        data = data_parser.get_info_forex(from_symbol='EUR',to_symbol='GBP',interval=60)
        data = data_parser.get_info_forex(from_symbol='GBP',to_symbol='AUD',interval=60)
        print('5 and sleep')
        sleep(70)
        print(datetime1)

        data = data_parser.get_info_forex(from_symbol='GBP',to_symbol='NZD',interval=60)
        data = data_parser.get_info_forex(from_symbol='USD',to_symbol='CAD',interval=60)
        data = data_parser.get_info_forex(from_symbol='AUD',to_symbol='CHF',interval=60)
        data = data_parser.get_info_forex(from_symbol='AUD',to_symbol='USD',interval=60)
        data = data_parser.get_info_forex(from_symbol='EUR',to_symbol='CAD',interval=60)
        print('10')
        sleep(70)
        print(datetime1)

        data = data_parser.get_info_forex(from_symbol='EUR',to_symbol='JPY',interval=60)
        data = data_parser.get_info_forex(from_symbol='GBP',to_symbol='CHF',interval=60)
        data = data_parser.get_info_forex(from_symbol='NZD',to_symbol='JPY',interval=60)
        data = data_parser.get_info_forex(from_symbol='USD',to_symbol='CHF',interval=60)
        data = data_parser.get_info_forex(from_symbol='AUD',to_symbol='JPY',interval=60)
        print('15')
        sleep(70)
        print(datetime1)

        # data = data_parser.get_info_forex(from_symbol='CAD',to_symbol='JPY',interval=60)
        # data = data_parser.get_info_forex(from_symbol='EUR',to_symbol='CHF',interval=60)
        # data = data_parser.get_info_forex(from_symbol='EUR',to_symbol='USD',interval=60)
        # data = data_parser.get_info_forex(from_symbol='GBP',to_symbol='JPY',interval=60)
        # data = data_parser.get_info_forex(from_symbol='NZD',to_symbol='USD',interval=60)
        # print('20')





def check_prediction_forex():

    file_winrate = open('logs/winrate_forex','r')
    winrate_lines = file_winrate.readlines()
    total = int(winrate_lines[0])
    win = int(winrate_lines[1])
    loss = int(winrate_lines[2])
    count_str = sum(1 for line in open('logs/prediction_forex', 'r'))
    file = open('logs/prediction_forex','r')

    i = 0
    lines = file.readlines()
    while (i < (count_str)):
        line = lines[i]
        print(line)
        res = tuple(map(str, line.split(' ')))  # convert to tuple

        with io.open(f'Forex_exchange/{res[0]}', encoding='utf-8') as file_stat:

            for line in file_stat:
                if f'{res[1]} {res[2]}' in line:  # ищем
                    curr = tuple(map(str, line.split(',')))

                    next = tuple(map(str, file_stat.__next__().split(',')))
                    total += 1
                    if (res[3] == 'sell\n'):
                        if (float(curr[4]) < float(next[4])):
                            win += 1
                        else:
                            loss += 1
                    else:
                        if (float(curr[4]) > float(next[4])):
                            win += 1
                        else:
                            loss += 1
        i += 1

    file_winrate = open('logs/winrate_forex','w')
    file_winrate.write(f'{str(total)}\n')
    file_winrate.write(f'{str(win)}\n')
    file_winrate.write(f'{str(loss)}\n')

    file = open('logs/prediction_forex', 'w')
    file.write('')
    file.close()
    file_winrate.close()



        # if len(lines) >= 2:  # Оценка наличия хотя бы двух строк в конце, чтобы гарантировать, что последняя строка завершена
        #     last_line = lines[-1]
        #     print(f'len line {len(lines)}')
        #     print(f'len line {lines[-1]}')



if __name__ == '__main__':
    runstrat()

