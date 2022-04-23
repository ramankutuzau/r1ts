from Calculate import convert_bar


# return 0 = не сработал
# return 1 = вверх
# return 2 = вниз

def check(open, close, high, low):
    bar = convert_bar.bar_to_points(open=open, close=close,
                                    high=high, low=low)
    if (bar[0] > 0):  # GREEN
        if ((bar[2] * -1) > (bar[0] * 2)):  # если нижняя тень х2 больше бара
            if (bar[1] <= (bar[0] * 0.5) and (bar[1] > 0)):
                # верхня тень меньше половины тела но она есть
                print(f'pin_bar GREEN')
                return 1
    elif (bar[0] < 0):  # RED
        if ((bar[1]) > (bar[0] * -1 * 2)):  # если верхняя тень х2 больше бара
            if ((bar[2] * -1) <= ((bar[0] * -1) * 0.5) and ((bar[2] * -1) > 0)):
                # нижняя тень меньше половины тела но она есть
                print(f'pin_bar RED')
                return 2
    else:
        return 0
