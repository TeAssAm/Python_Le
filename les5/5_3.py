with open('zrp.txt', 'r') as file:
    sal = []
    fml = []
    my_list = file.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
           fml.append(i[0])
        sal.append(i[1])
print(f' Оклад < 20000 {fml}, средний оклад {sum(map(int, sal)) / len(sal)}')