from Calculate import convert_bar


# return 0 = не сработал
# return 1 = вверх
# return 2 = вниз

def check(open, close, high, low,sma_30):
    bar = convert_bar.bar_to_points(open=open, close=close,
                                    high=high, low=low)
    if (abs(bar[2]) > (bar[0] * 2)):  # если нижняя тень х2 больше бара
        if (close > sma_30): #
            # print(f'pin_bar GREEN')
            return 1
    elif((bar[1]) > (abs(bar[0]) * 2)):  # если верхняя тень х2 больше бара
        if (close < sma_30):
            # print(f'pin_bar RED')
            return 2
    else:
        return 0
