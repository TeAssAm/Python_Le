def  x_pow(x, y):
    return 1 / x ** abs(y)

print(f'Результат  = {x_pow(int(input("X: ")), int(input("Y: ")))}')
