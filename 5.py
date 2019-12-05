prf = int(input("Выручка : "))
cost = int(input("Издержка: "))
bal = prf - cost
print(f" Финансовый результат: {bal}")
if bal > 0:
    print(f" Находимся в плюсе")
    rent = bal/prf
    print(rent)
    work = int(input("Количество сотрудников: "))
    print(f"{bal/work} на 1 сотрудника")
elif bal == 0:
    print("Гармония")
else:
    print("Убыточно")