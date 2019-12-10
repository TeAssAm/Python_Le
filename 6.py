a = float(input("Км 1го дня: "))
b = float(input("Таргет-цель: "))
day = 1
while a < b:
    a = a + a/10
    day += 1
    if a >= b:
        break
    if a < b:
        continue
print(day)