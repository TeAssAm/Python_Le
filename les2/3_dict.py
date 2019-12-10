s_list = ['Зима', 'Весна', 'Лето', 'Осень']
s_dict = {1 : 'Зима', 2 : 'Весна', 3 : 'Лето', 4 : 'Осень'}
month = int(input("Введите номер месяца : "))
if month ==1 or month == 2 or month == 12:
        print(s_dict.get(1))
        print(s_list[0])
elif month == 3 or month == 4 or month ==5:
    print(s_dict.get(2))
    print(s_list[1])
elif month == 6 or month == 7 or month == 8:
    print(s_dict.get(3))
    print(s_list[2])
elif month == 9 or month == 10 or month == 11:
    print(s_dict.get(4))
    print(s_list[3])
else:
    print("Такого месяца не существует")