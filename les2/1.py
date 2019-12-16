s1 = 6
s2 = 0.333
s3 = complex(1, 3)
s4 = "простая строка"
s5 = ['wsad', '1234']
s6 = ('qwerty', '3213')
s7 = {'Color1': 'Red', 'Color2': 'Blue'}
list = [s1, s2, s3, s4, s5, s6,s7]
for i in list:
    print(f'{i} is {type(i)}')