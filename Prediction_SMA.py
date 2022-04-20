from Data import Processes
# import Points_SMA

class Strategy_SMA():

    # def __init__(self,search,up,down,sma):
    #
    #     self.check_one_bar(search,up,down,sma)
    #     self.hui = 2



        # self.check_one_bar()

    def check_one_bar(search,up,down,sma,next):
        data = Processes().reade_txt()

        search_el = search
        shadow_up = up
        shadow_down = down

        found_list = []

        positive_list = []
        negative_list = []

        # print(f'пришла дата {data}') work
        print(f'ищем эелемент {search_el} up {shadow_up} down {shadow_down} sma {sma} next {next}') # work
        for el in data:
            if(el[0] == search_el)  and (el[3] == sma):
                # print(f'нашли эелментs {el}') # work
                found_list.append(el)
                # print(el)

        for el in found_list:
            if(el[4] >= 0):
                positive_list.append(el)
                # print(f'найденые в ++++ {el}')
            else:
                # print(f'найденые в ---- {el}')

                negative_list.append(el)





        # average_positive = Strategy_SMA.average(positive_list)
        # average_negative = Strategy_SMA.average(negative_list)

        result = Strategy_SMA.count_to_percent(len(positive_list),len(negative_list))

        print(f'result default check {len(positive_list)}/{len(negative_list)}')
        print(f'result in percent check {result}')
        # print(f'result default check: {result}')
        # print(f'count_positive: {count_positive} count_negative: {count_negative}')


        result_positive = Strategy_SMA.addition_check(found_list=positive_list,
                                             shadow_up=shadow_up,
                                             shadow_down=shadow_down,
                                             sma=sma)

        result_negative = Strategy_SMA.addition_check(found_list=negative_list,
                                                      shadow_up=shadow_up,
                                                      shadow_down=shadow_down,
                                                      sma=sma)

        result = Strategy_SMA.count_to_percent(result_positive,result_negative)
        print(f'result additional check {result_positive}/{result_negative}')
        print(f'result in percent check {result}')
        if (result_positive >= result_negative):
            return 1
        else:
            return 0
        # print(f'len positive ({count_positive}) len negative {count_negative}')
        # print(f'result {result}')
        # if(result > 0):
        #     return 1
        # else:
        #     return 0



        # if(len(self.positive_list) > len(self.negative_list)):
        #     print(f'Maybe: + {average_positive}')
        #
        # elif(len(self.positive_list) < len(self.negative_list)):
        #     print(f'Maybe: - {average_negative}')



    def average(list):
        sum = 0.0
        for el in list:
            sum += el
        len_list = len(list)
        if(len_list == 0): # if positive/negative count == 0
            len_list = 1
        return round(sum/len_list,2)

    def addition_check(found_list,shadow_up,shadow_down,sma):
        count_list = []
        for el in found_list:
            # print(f'приходит {el}')
            if (el[0] >= 0.0):
                if (el[2] == shadow_down) and (el[3] == sma):
                    count_list.append(el)
            else:
                if (el[1] == shadow_up) and (el[3] == sma):
                     count_list.append(el)

        return len(count_list)
        # print(f'Additional check: {len(positive_list)}/{len(negative_list)}')
        # print(f'    : {self.count_to_percent(len(positive_list),len(negative_list))}')


    def count_to_percent(positive_count,negative_count):
        hundred_per = positive_count + negative_count
        if not (hundred_per == 0):
            hundred_per = 100 / hundred_per

        positive = round(positive_count * hundred_per,1)
        negative = round(negative_count * hundred_per,1)
        return (positive,negative)