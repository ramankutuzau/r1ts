


from Calculate import convert_bar
# return 0 = не сработал
# return 1 = вверх
# return 2 = вниз

def check(open,close,high,low,prev_open,prev_close,prev_high,prev_low):

    bar = convert_bar.bar_to_percent(open=open,close=close,high=high,low=low)
    prev_bar = convert_bar.bar_to_percent(open=prev_open,close=prev_close,high=prev_high,low=prev_low)


    if(bar[0] > 0.1): # GREEN
        if(prev_bar[0] < 0.1):
            if(bar[0] / 100 * 80 <= abs(prev_bar[0])) and (bar[0] / 100 * 120 >= abs(prev_bar[0])):

                # print('rails_bar GREEN')
                return 1
    elif(bar[0] < -0.1):
        if(prev_bar[0] > 0.1):
            if(abs(bar[0]) / 100 * 80 <= prev_bar[0]) and (abs(bar[0]) / 100 * 120 >= prev_bar[0]):

                # print('rails_bar RED')
                return 2

    else:
        return 0
