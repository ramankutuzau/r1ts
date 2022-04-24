

from Calculate import convert_bar
from Strategies.Patterns import inside_bar


# return 0 = не сработал
# return 1 = вверх
# return 2 = вниз

def check(open,close,high,low,prev_open,prev_close,prev_high,prev_low,prev2_open,prev2_close,prev2_high,prev2_low):
    bar = convert_bar.bar_to_points(open=open,close=close,high=high,low=low)
    prev_bar = convert_bar.bar_to_points(open=prev_open,close=prev_close,high=prev_high,low=prev_low)
    prev2_bar = convert_bar.bar_to_points(open=prev2_open,close=prev2_close,high=prev2_high,low=prev2_low)
    # ищем инсайд бары
    result = inside_bar.check(open=prev_open, close=prev_close, high=prev_high, low=prev_low,
                              prev_open=prev2_open, prev_close=prev2_close, prev_high=prev2_high,
                              prev_low=prev2_low)
    # вернулся GREEN ( BUY ) значит на падение
    if(result == 1):
        if (high >= prev2_high):  # максимум третьего выше первого ( материнского )
            # print(f'fake_bar RED')

            return 2
    #  вернулся RED ( SELL ) значит на РОСТ
    elif(result == 2):
        if(open <= prev2_close): # третий бар меньше первого
            if(low < prev2_low): # минимум первого меньшетретьего ( материнского )

                # print(f'fake_bar GREEN')
                return 1
    else:
        return 0
