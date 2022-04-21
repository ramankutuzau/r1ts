

def bar_to_percent(open,high,low,close):

    # if (type == 'percent'):
    body = to_percent(data_up=close, data_down=open)  # bar +/-
    shadows = calculate_shadows(body=body,dataopen=open,dataclose=close,
                                         datahigh=high,datalow=low)

    # elif(type == 'points'):
    #     body = to_points(dataclose=close, dataopen=open)  # bar +/-
    #     shadows = calculate_shadows(body=body,dataopen=open,dataclose=close,
    #                                      datahigh=high,datalow=low)
    #

    bar = (body,shadows[0],shadows[1])
    return bar





def to_percent(data_up,data_down):
    difference = data_up - data_down
    percent = round(round(difference * 10000) / 100,2)
    return percent

def to_points(dataclose,dataopen):
    points = dataclose - dataopen
    return int(points * 100000)

def shadow_in_points(x,y):
    points = x - y
    return int(points * 100000)

def calculate_shadows(body,dataopen,dataclose,datahigh,datalow):
    up = 0.0
    down = 0.0
    if (body > 0.0):
        up = to_percent(datahigh,dataclose)
        down = to_percent(dataopen,datalow) * -1
    elif(body < 0.0):
        up = to_percent(datahigh,dataopen)
        down = to_percent(dataclose,datalow) * -1
    elif(body == 0.0):
        up = to_percent(datahigh,dataclose)
        down = to_percent(dataopen,datalow) * -1

    return (up,down)
