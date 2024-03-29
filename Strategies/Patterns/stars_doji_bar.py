

from Calculate import convert_bar

# return 0 = не сработал
# return 1 = вверх
# return 2 = вниз

def check(open,close,high,low,prev_open,prev_close,prev_high,prev_low,prev2_open,prev2_close,prev2_high,prev2_low):
    bar = convert_bar.bar_to_points(open=open,close=close,high=high,low=low)
    prev_bar = convert_bar.bar_to_points(open=prev_open,close=prev_close,high=prev_high,low=prev_low)
    prev2_bar = convert_bar.bar_to_points(open=prev2_open,close=prev2_close,high=prev2_high,low=prev2_low)

    if (bar[0] > 0):  # last GREEN
        if(prev_bar[1] > (abs(prev_bar[0]) * 2) ) and (abs(prev_bar[2]) > (abs(prev_bar[0]) * 2) ): # бар по середине с большими тенями
            if(close < prev2_open): # последний бар меньше материнского
                if((bar[0] * 2 ) <= abs(prev2_bar[0])): # в 2 раза меньше материнской свечи

                    # print(f'doji_bar GREEN')
                    return 1

    elif (bar[0] < 0):  # last RED
        if(prev_bar[1] > (abs(prev_bar[0]) * 2) ) and (abs(prev_bar[2]) > (abs(prev_bar[0]) * 2) ): # бар по середине с большими тенями
            if(close > prev2_open): # последний бар меньше материнского
                if (abs(bar[0] * 2) <= prev2_bar[0]):  # в 2 раза меньше материнской свечи

                    # print(f'doji_bar RED')
                    return 2


    else:
        return 0
