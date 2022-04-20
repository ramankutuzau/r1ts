
class Processes():

    def __init__(self,data):
        self.data = data
        self.create_txt()
        self.count = 0

    def create_txt(self):
        # f = open('USDSEK2015-2022-bars.txt', 'a') дозапись
        count = 0
        f = open('USDSEK2015-2022-bars.txt', 'w')
        for index in self.data:
            count += 1
            print(f'count: {count}')
            print(f'пришло {index[0]},{index[1]},{index[2]}')
            str_write = f'{index[0][0]},{index[0][1]},{index[0][2]},{index[0][3]},{index[0][4]},' \
                        f'{index[1][0]},{index[1][1]},{index[1][2]},{index[1][3]},{index[0][4]},' \
                        f'{index[2][0]},{index[2][1]},{index[2][2]},{index[2][3]},{index[0][4]} \n'
            print(f'записал {str_write}')
            f.write(str_write)
        f.close()
        print('IS COMPLETE')

        # for index in self.data:
        #     # print(index)
        #     f.write(str(index) +'\n')
        # f.close()

    def reade_txt(self):
        f = open('USDSEK2015-2022-bars.txt')
        data = []
        for line in f:
            res = tuple(map(float, line.split(',')))
            # print(f'res {res}')
            prev_bar = (res[0],res[1],res[2],res[3],res[4])
            current_bar = (res[5],res[6],res[7],res[8],res[9])
            result_bar = (res[10],res[11],res[12],res[13],res[14])
            res = (prev_bar,current_bar,result_bar)
            data.append(res)
            # print(res)

        return data
    # printing result
    # print("Tuple after getting conversion from String : " + str(res))
