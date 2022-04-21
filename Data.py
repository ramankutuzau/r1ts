
class Processes():

    # def __init__(self,data):
    #     self.data = data
    #     self.create_txt()
    #     self.count = 0

    def create_txt(self):
        count = 0
        f = open('GBPUSD_2018-2022-bars.csv', 'w') # 'a' дозапись
        for index in self.data:
            count += 1
            print(f'count: {count}')
            print(f'пришло {index[0]},{index[1]},{index[2]},{index[3]}')
            str_write = f'{index[0][0]},{index[0][1]},{index[0][2]},{index[0][3]},{index[0][4]},{index[0][5]},{index[0][6]},{index[0][7]},{index[0][8]},' \
                        f'{index[1][0]},{index[1][1]},{index[1][2]},{index[1][3]},{index[0][4]},{index[0][5]},{index[0][6]},{index[0][7]},{index[0][8]},' \
                        f'{index[2][0]},{index[2][1]},{index[2][2]},{index[2][3]},{index[0][4]},{index[0][5]},{index[0][6]},{index[0][7]},{index[0][8]},' \
                        f'{index[3][0]},{index[3][1]},{index[3][2]},{index[3][3]},{index[3][4]},{index[0][5]},{index[0][6]},{index[0][7]},{index[0][8]}\n'
                            # body       #shadow_up   #shadow_down   #sma (30)     # sma (200)   #r1           #r2           #s1           #s2
            print(f'записал {str_write}')
            f.write(str_write)
        f.close()
        print('IS COMPLETE')

        # for index in self.data:
        #     # print(index)
        #     f.write(str(index) +'\n')
        # f.close()

    def reade_txt(self):
        f = open('GBPUSD_2018-2022-bars.csv')
        data = []
        for line in f:
            res = tuple(map(float, line.split(',')))
            # print(f'res {res}')
            #            body   up     down  sma30  sma200  r1     r2     s1      s2
            bar = (res[0],res[1],res[2],res[3],res[4],res[5],res[6],res[7],res[8])
            bar1 = (res[9],res[10],res[11],res[12],res[13],res[14],res[15],res[16],res[17])
            bar2 = (res[18],res[19],res[20],res[21],res[22],res[23],res[24],res[25],res[26])
            bar3 = (res[27],res[28],res[29],res[30],res[31],res[32],res[33],res[34],res[35])
            res = (bar3,bar2,bar1,bar)
            data.append(res)
            # print(res)

        return data
    # printing result
    # print("Tuple after getting conversion from String : " + str(res))
