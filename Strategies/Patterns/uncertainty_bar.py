


from Calculate import convert_bar
# return 0 = не сработал
# return 1 = вверх
# return 2 = вниз

def check(open,close,high,low,prev_open,prev_close,prev_high,prev_low):

    bar = convert_bar.bar_to_points(open=open,close=close,high=high,low=low)
    prev_bar = convert_bar.bar_to_points(open=prev_open,close=prev_close,high=prev_high,low=prev_low)

    # GREEN ( BUY )
    if(prev_bar[0] > 1) or (prev_bar[0] < -1): # тело есть green/red
        if(prev_bar[1] > (prev_bar[0] * 2))  : # верхня тень больше бара в 2 раза ( предыдущего )
            if((prev_bar[2] * -1 ) > (prev_bar[0] * 2))  : # нижняя тень больше бара в 2 раза ( предыдущего )
                if(close > prev_high): # если выше максимума предыдущей свечи

                    # print(f'uncertainty_bar GREEN')
                    return 1
                # RED ( SELL )
                elif(close < prev_low):  # если ниже максимума предыдущей свечи

                    # print(f'uncertainty_bar RED')
                    return 2

    else:
       return 0
