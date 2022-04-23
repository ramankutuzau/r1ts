

from Calculate import convert_bar
# return 0 = не сработал
# return 1 = вверх
# return 2 = вниз

def check(open,close,high,low,prev_open,prev_close,prev_high,prev_low,prev2_open,prev2_close,prev2_high,prev2_low):
    bar = convert_bar.bar_to_points(open=open,close=close,high=high,low=low)
    prev_bar = convert_bar.bar_to_points(open=prev_open,close=prev_close,high=prev_high,low=prev_low)
    prev2_bar = convert_bar.bar_to_points(open=prev2_open,close=prev2_close,high=prev2_high,low=prev2_low)


    if (close > prev_close):  # GREEN
        if(prev_close > prev2_close):
            if(prev2_bar[0] > 1):
                print(f'crows_soldiers_bar GREEN')
                return 1

    elif (close < prev_close):  # last RED
        if(prev_close < prev2_close):
            if(prev2_bar [0] < -1):
                print(f'crows_soldiers_bar RED')
                return 2
    else:
        return 0
