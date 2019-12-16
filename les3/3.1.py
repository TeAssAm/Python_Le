def div(*args):

    try:
        arg1 = int(input("Число1 "))
        arg2 = int(input("Число2 "))
        res = arg1 / arg2
    except ValueError:
        return 'Ошибка'
    except ZeroDivisionError:
        return "Деление на 0 невозможно"

    return res


    if arg2 != 0:
        return arg1 / arg2
    else:
        print("Деление на 0 невозможно")



print(f'result  {div()}')