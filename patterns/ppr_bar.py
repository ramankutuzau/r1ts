


from calculate import convert_bar
# return 0 = не сработал
# return 1 = вверх
# return 2 = вниз

def check(open,close,high,low,prev_open,prev_close,prev_high,prev_low):

    bar = convert_bar.bar_to_points(open=open,close=close,high=high,low=low)
    prev_bar = convert_bar.bar_to_points(open=prev_open,close=prev_close,high=prev_high,low=prev_low)


    if(bar[0] > 0) and (prev_bar[0] < 0): # GREEN
        if(close > prev_open) and (open <= prev_close): # сама свеча должна быть больше ( поглощения )
            if(bar[1] > 0) and (prev_bar[1] > 0): # верхние тени есть
                if(bar[2] < 0) and (prev_bar[2] < 0): # нижние тени есть
                    if(low < prev_low): # нижяя тень последего ниже предыдущего
                        if(close > prev_high): # цена закрытие больше предыдущего максимума
                            # print(f'ppr_bar GREEN ')
                            return 1
                        # RED
                        elif(close < prev_low):  # цена закрытие меньше предыдущего минимуго
                            # print(f'ppr_bar RED ')
                            return 2

    else:
        return 0
