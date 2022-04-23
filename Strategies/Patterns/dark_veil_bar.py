

from Calculate import convert_bar
# return 0 = не сработал
# return 1 = вверх
# return 2 = вниз

def check(open,close,high,low,prev_open,prev_close,prev_high,prev_low):
    bar = convert_bar.bar_to_points(open=open, close=close, high=high, low=low)
    bar_percent = convert_bar.bar_to_percent(open=open, close=close, high=high, low=low)
    prev_bar = convert_bar.bar_to_points(open=prev_open, close=prev_close, high=prev_high, low=prev_low)
    prev_bar_percent = convert_bar.bar_to_percent(open=prev_open, close=prev_close, high=prev_high, low=prev_low)

    if(bar[0] > 0) and (prev_bar[0] < 0):  # GREEN
        if(abs(bar_percent[0]) > 0.05) and (abs(prev_bar_percent[0]) > 0.05):
            if(open < prev_low): # октрылась ниже чем минимум предыдущей ( гэп )
                if(bar[0] > abs(prev_bar[0]) * 0.5): # больше половины предыдущей свечи
                    print('dark_veil_bar GREEN')
                    return 1

    elif (bar[0] < 0) and (prev_bar[0] > 0):  # RED
        if(abs(bar_percent[0]) > 0.05) and (abs(prev_bar_percent[0]) > 0.05):
            if(open > prev_high): # октрылась выше чем закрылась предыдущая ( гэп )
                if(abs(bar[0]) > prev_bar[0] * 0.5): # больше половины предыдущей свечи
                    print('dark_veil_bar RED')
                    return 2
    else:
        return 0
