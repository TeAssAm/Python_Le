def my_func(arg1 , arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 > arg2 and arg2 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3

print(f'Результат = {my_func(int(input("1ый аргумент: ")), int(input("2ый аргумент: ")), int(input("3ый аргумент: ")))}')
