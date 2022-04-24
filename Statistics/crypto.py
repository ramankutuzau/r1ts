import backtrader as bt
from Strategies import all_patterns
import os

def create(data,symbol):

    cerebro = bt.Cerebro()

    cerebro.adddata(data)

    # cerebro.resampledata(data)
    create_temp_files()

    with open('Strategies/timeframe', 'w') as f:
        f.write("%Y-%m-%d")
    cerebro.addstrategy(all_patterns.Strategy)
    cerebro.run()
    rename_template_files(symbol=symbol)
    os.remove('Strategies/timeframe')

    # cerebro.plot(style='bar', volume=False)


def create_temp_files():
    file_curr = open(f'current_temp','w')
    file_curr.close()

    file_history = open(f'history_temp','w')
    file_history.write("pin_bar:0,0,0\n")
    file_history.write("inside_bar:0,0,0\n")
    file_history.write("outside_bar:0,0,0\n")
    file_history.write("ppr_bar:0,0,0\n")
    # file_history.write("uncertainty_bar:0,0\n")
    file_history.write("uncertainty_2_bar:0,0,0\n")
    file_history.write("takeovers_bar:0,0,0\n")
    file_history.write("fake_bar:0,0,0\n")
    file_history.write("stars_bar:0,0,0\n")
    file_history.write("stars_doji_bar:0,0,0\n")
    file_history.write("crows_soldier_bar:0,0,0\n")
    file_history.write("rails_bar:0,0,0\n")
    file_history.write("tweezers_bar:0,0,0\n")
    file_history.write("dark_veil_bar:0,0,0\n")
    file_history.write("capture_belt_bar:0,0,0\n")
    file_history.close()


def rename_template_files(symbol):

    os.rename('history_temp', f'Crypto_exchange/Statistics/history_{symbol}')
    os.rename('current_temp', f'Crypto_exchange/Current/current_{symbol}')

