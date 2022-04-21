


from calculate import convert_bar
# return 0 = не сработал
# return 1 = вверх
# return 2 = вниз

def check(bar,prev_bar,dataclose_curr,dataopen_prev):
    if(bar[0] < 0.0) and (prev_bar[0] > 0.0): # RED
        if(bar[1] > prev_bar[1]) and (bar[1] >= 0.01): # максимум выше и 2 тени есть
            if(bar[2] < prev_bar[2]) and (bar[1] <= 0.01): # минимум нижу и тень есть bar #2
                if(dataclose_curr < dataopen_prev): # ниже/больше предыдущего
                    # print(f'RED {bar} > {prev_bar}')
                    return 2
    elif(bar[0] > 0.0): # GREEN
        if(bar[1] > prev_bar[1]) and (bar[1] >= 0.01): # максимум выше и 2 тени есть
            if(bar[2] < prev_bar[2]) and (bar[1] <= 0.01): # минимум нижу и тень есть
                if(bar[0]  > (prev_bar[0] * -1)): # выше/больше предыдущего
                    if (dataclose_curr > dataopen_prev):  # ниже/больше предыдущего
                        # print(f'GREEN {bar} > {prev_bar}')
                        return 1
    else:
        return 0
