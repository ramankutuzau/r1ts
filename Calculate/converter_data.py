def csv_converter(filename,exchange):
    f = open(f'{exchange}_exchange/{filename}','r')
    data = []
    for line in f:
        data.append(line)
    i = 1
    f = open(f'{exchange}_exchange/{filename}','w')
    f.write(data[0])
    while i < len(data) - 1:
        f.write(data[len(data) - i - 1])
        i += 1
    # print(data)
    f.close()
