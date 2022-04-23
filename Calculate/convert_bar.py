

def bar_to_percent(open,high,low,close):

    body = to_percent(data_up=close, data_down=open)  # bar +/-
    shadows = calculate_shadows(body=body,dataopen=open,dataclose=close,
                                         datahigh=high,datalow=low)

    bar = (body,shadows[0],shadows[1])
    return bar

def bar_to_points(open,high,low,close):


    body = to_points(dataclose=close, dataopen=open)  # bar +/-
    shadows = shadow_in_points(body=body,open=open,close=close,
                                         high=high,low=low)


    bar = (body,shadows[0],shadows[1])
    return bar






def shadow_in_points(body,open,close,high,low):
    up = 0
    down = 0
    if (body > 0):
        up = to_points(high,close)
        down = to_points(open,low) * -1
    elif(body < 0):
        up = to_points(high,open)
        down = to_points(close,low) * -1
    elif(body == 0):
        up = to_points(high,close)
        down = to_points(open,low) * -1

    return (up,down)


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

def to_percent(data_up,data_down):
    difference = data_up - data_down
    percent = round(round(difference * 10000) / 100,2)
    return percent

def to_points(dataclose,dataopen):
    points = dataclose - dataopen
    return round(points * 100000)