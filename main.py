from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import os.path  # To manage paths
import sys  # To find out the script name (in argv[0])
import argparse
import backtrader as bt
# from Strategies import all_patterns
import requests
import data_parser

from Calculate import converter_data



def runstrat():

    cerebro = bt.Cerebro()

    data = data_parser.get_info_forex(from_symbol='GBP',to_symbol='USD',interval=60)
    cerebro.adddata(data)






if __name__ == '__main__':
    runstrat()
