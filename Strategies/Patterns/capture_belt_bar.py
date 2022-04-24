

from Calculate import convert_bar
# return 0 = не сработал
# return 1 = вверх
# return 2 = вниз

def check(open,close,high,low):
    bar = convert_bar.bar_to_points(open=open, close=close, high=high, low=low)

    if(bar[0] > 0):  # GREEN
        if(bar[1] > 0 ): # верхняя тень есть
            if(open == low ): # открылась и не опускалась
                # print('capture_belt_bar GREEN')
                return 1
    elif(bar[0] < 0):  # RED
        if(bar[2] < 0 ): # нижняя тень есть
            if(open == high ): # открылась и не поднималась
                # print('capture_belt_bar RED')

                return 2
    else:
        return 0
