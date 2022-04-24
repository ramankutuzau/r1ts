


from Calculate import convert_bar
# return 0 = не сработал
# return 1 = вверх
# return 2 = вниз

def check(open,close,high,low,prev_open,prev_close,prev_high,prev_low):

    bar = convert_bar.bar_to_points(open=open,close=close,high=high,low=low)
    prev_bar = convert_bar.bar_to_points(open=prev_open,close=prev_close,high=prev_high,low=prev_low)


    if(bar[0] > 0) and (prev_bar[0] < 0): # GREEN тела есть
        if(close > prev_open) and (open <= prev_close): # сама свеча должна быть больше ( поглощения )
            if(bar[0] > (abs(prev_bar[0]) * 2) ): # зеленое больше в 2 раза
                # print(f'takeovers_bar GREEN ')
                return 1
    elif(bar[0] < 0)  and (prev_bar[0] > 0): # RED тела есть
        if (close > prev_open) and (open <= prev_close):  # сама свеча должна быть больше ( поглощения )
            if (bar[0] > (abs(prev_bar[0]) * 2)):  # красное больше в 2 раза

                # print(f'takeovers_bar RED ')
                return 2

    else:
        return 0