def sum ():
    sum_res = 0
    ex = False
    while ex == False:
        number = input('Введите числа или B  - ').split()
        res = 0
        for el in range(len(number)):
            if number[el] == 'B' or number[el] == 'b':
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Сумма** {sum_res}')
    print(f'Финальная сумма {sum_res}')

sum()