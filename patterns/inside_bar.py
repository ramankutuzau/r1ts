

from calculate import convert_bar
# return 0 = не сработал
# return 1 = вверх
# return 2 = вниз

def check(open,close,high,low,prev_open,prev_close,prev_high,prev_low):
    bar = convert_bar.bar_to_percent(open=open,close=close,high=high,low=low)
    prev_bar = convert_bar.bar_to_percent(open=prev_open,close=prev_close,high=prev_high,low=prev_low)
    if(bar[0] < 0.0): # RED
        if((bar[0] * -1 * 2) <= prev_bar[0]): # внутренний бар меньше в 2 раза материнского бара
            if(bar[1] >= 0.01 and prev_bar[1] >= 0.01): # верхние шипы есть
                if ((bar[2] * -1) >= 0.01 and (prev_bar[2] * -1) >= 0.01): # нижние шипы есть
                    if(open <= prev_close): # внутренний бар ниже/равен закрытию материнского
                        if(high <= prev_high): # верхние шипы не выходят за шип материнского
                            if(low > prev_open): # нижний пиш не выходит за открытие материнского бара
                                # print(f'RED {bar} < {prev_bar}')
                                return 2
    elif (bar[0] > 0.0):  # GREEN
        if ((bar[0] * 2) <= (prev_bar[0] * -1)):  # внутренний бар меньше в 2 раза материнского бара
            if (bar[1] >= 0.01 and prev_bar[1] >= 0.01): # верхние шипы есть
                if ((bar[2] * -1) >= 0.01 and (prev_bar[2] * -1) >= 0.01): # нижние шипы есть
                    if (open >= prev_close):  # внутренний бар ниже/равен закрытию материнского
                        if (high <= prev_high):  # верхние шипы не выходят за шип материнского
                            if (low >= prev_low):  # нижний пиш не выходит за открытие материнского бара
                                # print(f'GREEN {bar} > {prev_bar}')

                                return 1
    else:
        return 0