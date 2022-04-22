import aifc

import all_patterns
from Data import Processes
# import Points_SMA

class Strategy_SMA():

    # def __init__(self):
    #     self.positive_list = []
    #     self.negative_list = []
    #     self.win = 0
    #     self.no_win = 0



        # self.check_one_bar()

    def check_gap(self,bar,bar1):
        print('count')
        if(bar > bar1):
            difference = bar1 - bar
            percent = round(round(difference * 10000) / 100, 4)
            print(percent)
            if(percent <= -0.02):
                print('gap вниз')
                print(f'{bar} < {bar1})')


    def check_three_bars(self,bar,bar1,bar2,bar3):
        data = Processes().reade_txt()
        # print(f'search: {search_bar})')
        # print(f'prev: {prev_bar}')
        # print(f'next: {next_bar}')

        found_list = []

        positive_list = []
        negative_list = []
        # data = None
        # print(f'ищем эелемент {search_el} up {shadow_up} down {shadow_down} sma {sma} next {next}') # work
        # print(len(data))
        i = 0
        succesfull = 0
        while i < len(data):
            # print(f'data: {data[i]}')
            three_bars = data[i]
            if (three_bars[2][0] == bar1[0]):  # body
                if (three_bars[1][0] == bar2[0]):  # up
                    if (three_bars[0][0] == bar3[0]):  # down

                        # if (three_bars[2][3] == bar1[3]):  # sma30
                            # if (three_bars[2][4] == bar1[4]):  # sma200

                                # if (three_bars[2][5    succesfull += 1
                        #                                                     if (three_bars[3][0] >= 0.0):
                        #                                                         positive_list.append(three_bars[2][0])
                        #                                                     else:
                        #                                                         negative_list.append(three_bars[2][0]) ee_bars[2][8] == bar1[8]):  # s2
                                                succesfull += 1
                                                if (three_bars[3][0] >= 0.0):
                                                    positive_list.append(three_bars[2][0])
                                                else:
                                                    negative_list.append(three_bars[2][0])

            # if (three_bars[2][0] == bar1[0]):  # body
            #     if (three_bars[1][0] == bar2[0]):  # body
            #         if (three_bars[0][2] == bar3[2]):  # body
            #
            #             if(three_bars[2][3] == bar1[3]):
            #                 if(three_bars[1][3] == bar2[3]):
            #                     if(three_bars[0][3] == bar3[3]):
            #
            #                         if (three_bars[2][5] == bar1[5]):
            #                             if (three_bars[2][6] == bar1[6]):
            #                                 if (three_bars[2][7] == bar1[7]):
            #                                     if (three_bars[2][8] == bar1[8]):



            #
            #                                     if (three_bars[1][0] == bar2[0]):  # body
            #                                         if (three_bars[1][1] == bar2[1]):  # body
            #                                             if (three_bars[1][2] == bar2[2]):  # body
            #                                                 if (three_bars[1][3] == bar2[3]):  # sma30
            #                                                     if (three_bars[1][4] == bar2[4]):  # sma200
            #                                                         if (three_bars[1][5] == bar2[5]):  # r1
            #                                                             if (three_bars[1][6] == bar2[6]):  # r2
            #                                                                 if (three_bars[1][7] == bar2[7]):  # s1
            #                                                                     if (three_bars[1][8] == bar2[8]):  # s2
            #
            #                                                                         succesfull += 1
            #                                                                         if (three_bars[3][0] >= 0.0):
            #                                                                             positive_list.append(three_bars[2][0])
            #                                                                         else:
            #                                                                             negative_list.append(three_bars[2][0])

            # print(three_bars)
            # print(three_bars)
            # # print(three_bars)
            # if(three_bars[1][0] == current_bar[0]):
            #     if(three_bars[0][0] == prev_bar[0]):
            #
            #         if(three_bars[0][3] == prev_bar[3]):
            #             if(three_bars[0][4] == prev_bar[4]):
            #
            #                 if(three_bars[0][1] == prev_bar[1]):
            #                     if(three_bars[0][2] == prev_bar[2]):
            #
            #                         if(three_bars[1][1] == current_bar[1]):
            #                             if(three_bars[1][2] == current_bar[2]):
            #
            #                                 if(three_bars[1][3] == current_bar[3]):
            #                                     if(three_bars[1][4] == current_bar[4]):
            #                                         succesfull += 1
            #                                         if (three_bars[2][0] >= 0.0):
            #                                             positive_list.append(three_bars[2][0])
            #                                         else:
            #                                             negative_list.append(three_bars[2][0])



                    # print(f'пришло {three_bars}')
                    # print(f'ищу {three_bars[1][0]} == {search_bar[0]})')
                    # print(f'и {three_bars[0][0]} == {prev_bar[0]})')
                # print(f' для {three_bars} где if 1 : {three_bars[1][0]} == {search_bar[0]} and if {three_bars[0][0]} == {prev_bar[0]})')
            i += 1
        print(f'searching : {succesfull}')
        # print(f'prev: {prev_bar[0]}, search {search_bar[0]}')

        print(f'positive : {len(positive_list)} negative: {len(negative_list)}')
        if (len(positive_list) > 0) or (len(negative_list) > 0):
            # count_negative = len(negative_list) * 1.5
            # count_positive = len(positive_list) * 1.5
            if(len(positive_list) >= len(negative_list)):
                Strategy_SMA.open_position(self,'buy',bar)
            elif(len(negative_list) > len(positive_list)):
                Strategy_SMA.open_position(self,'sell',bar)
        else:
            Strategy_SMA.open_position(self, 'no buy',bar)


        # for el in data:
        #     if(el[0] == search_bar[0]):
        #
        #         print(f'нашли эелментs {el}') # work
                # found_list.append(el)
                # print(el)
        #
        #
        #
        #
        #

        # average_positive = Strategy_SMA.average(positive_list)
        # average_negative = Strategy_SMA.average(negative_list)
        #
        # result = Strategy_SMA.count_to_percent(len(positive_list),len(negative_list))
        #
        # print(f'result default check {len(positive_list)}/{len(negative_list)}')
        # print(f'result in percent check {result}')
        # print(f'average positive: {average_positive} average negative: {average_negative}')


        # result_positive = Strategy_SMA.addition_check(found_list=positive_list,
        #                                      shadow_up=shadow_up,
        #                                      shadow_down=shadow_down,
        #                                      sma=sma)
        #
        # result_negative = Strategy_SMA.addition_check(found_list=negative_list,
        #                                               shadow_up=shadow_up,
        #                                               shadow_down=shadow_down,
        #                                               sma=sma)
        #
        # result = Strategy_SMA.count_to_percent(result_positive,result_negative)
        # print(f'result additional check {result_positive}/{result_negative}')
        # print(f'result in percent check {result}')



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

    def open_position(self,signal,next):
        print(f'{signal} result')
        f = open('result.txt')
        line = f.readlines()
        win = int(line[0])
        loss = int(line[1])
        miss = int(line[2])
        cash = float(line[3])
        buy = int(line[4])
        sell = int(line[5])
        f.close()

        if (signal == 'buy'):
            if (next[0] >= 0.0):
                cash += 0.7
                win += 1
                print(f"cash {cash} win buy")
                buy += 1
            else:
                buy += 1
                cash -= 1.0
                loss += 1
                print(f"cash {cash} loss buy")

        elif (signal == 'sell'):
            if (next[0] <= 0.0):
                win += 1
                cash += 0.7
                print(f"cash {cash} win sell")
                sell += 1
            else:
                sell += 1
                cash -= 1.0
                loss += 1
                print(f"cash {cash} loss sell")

        elif (signal == 'no buy'):
                miss += 1

        if(cash <= 0.0):
            print('pizda')
            print(cash)
            exit()
        f = open('result.txt','w')
        f.write(str(win)+'\n')
        f.write(str(loss)+'\n')
        f.write(str(miss)+'\n')
        f.write(str(cash)+'\n')
        f.write(str(buy)+'\n')
        f.write(str(sell)+'\n')
            # str_write = f'я продал, вниз next ⟶ {next} '
            # print(str_write)

