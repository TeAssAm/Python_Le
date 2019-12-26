def summary():
    try:
        with open('ch.txt', 'w+') as file1:
            line = input('Введите цифры через пробел \n')
            file1.writelines(line)
            numb = line.split()

            print(sum(map(int, numb)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно набран номер. Ошибка ввода-вывода')
summary()