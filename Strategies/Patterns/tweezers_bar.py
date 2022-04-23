

from Calculate import convert_bar
# return 0 = не сработал
# return 1 = вверх
# return 2 = вниз

def check(open,close,high,low,prev_open,prev_close,prev_high,prev_low):
    bar = convert_bar.bar_to_points(open=open,close=close,high=high,low=low)
    bar_percent = convert_bar.bar_to_percent(open=open,close=close,high=high,low=low)
    prev_bar = convert_bar.bar_to_points(open=prev_open,close=prev_close,high=prev_high,low=prev_low)
    prev_bar_percent = convert_bar.bar_to_percent(open=prev_open,close=prev_close,high=prev_high,low=prev_low)

    max = abs(bar_percent[0]) * 2
    min = abs(bar_percent[0]) / 2

    # GREEN
    if(abs(bar_percent[2]) > (abs(bar_percent[0]) * 3) ): # нижняя тень больше бара в 3 раза
        if((bar_percent[1] * 3) <  abs(bar_percent[2]) ): # верхняя тень в 3 раза меньше нижней
            if (abs(prev_bar_percent[2]) > (abs(prev_bar_percent[0]) * 2)):  # нижняя тень больше бара в 3 раза ( предыдущего )
                if (abs(prev_bar_percent[2]) > (prev_bar_percent[1] * 2)):  # нижняя тень больше верхней в 3 раза
                    if(abs(prev_bar_percent[0]) >= min) and (abs(prev_bar_percent[0]) <= max): # бары почти одинаковые
                        print('tweezers_bar GREEN')
                        return 1
    # RED
    elif (bar_percent[1] > (abs(bar_percent[0]) * 3) ): # верхняя тень больше бара в 3 раза
        if((abs(bar_percent[2]) * 3) <  bar_percent[1] ): # нижняя тень в 3 раза меньше верхней
            if (prev_bar_percent[1] > (abs(prev_bar_percent[0]) * 2)):  # верхняя тень больше бара в 3 раза ( предыдущего )
                if (prev_bar_percent[1] > (abs(prev_bar_percent[2]) * 2)):  # верхняя тень больше нижней в 3 раза
                    if(abs(prev_bar_percent[0]) >= min) and (abs(prev_bar_percent[0]) <= max): # бары почти одинаковые
                        print('tweezers_bar RED')
                        return 2
    else:
        return 0
