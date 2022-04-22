


from calculate import convert_bar
# return 0 = не сработал
# return 1 = вверх
# return 2 = вниз

def check(open,close,high,low,prev_open,prev_close,prev_high,prev_low):

    bar = convert_bar.bar_to_points(open=open,close=close,high=high,low=low)
    prev_bar = convert_bar.bar_to_points(open=prev_open,close=prev_close,high=prev_high,low=prev_low)

    # GREEN ( BUY )
    if(prev_bar[0] > 1) or (prev_bar[0] < -1): # тело предыдущего есть green/red
        if(prev_bar[1] > (prev_bar[0] * 2))  : # верхня тень больше бара в 2 раза
            if((prev_bar[2] * -1 ) > (prev_bar[0] * 2))  : # нижняя тень больше бара в 2 раза
                if(bar[0] > 1) or (bar[0] < -1):  # тело текущего есть последней есть green/red
                    if(low < prev_low): # если выше максимума предыдущей свечи
                        # print(f'uncertainty_bar_2 GREEN')
                        return 1
                    # RED ( SELL )
                    elif(high > prev_high):  # свеча проколола максимум предыдущей
                        # print(f'uncertainty_bar_2 RED')
                        return 2
    else:
        return 0
