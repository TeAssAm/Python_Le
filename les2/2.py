lst = []
n = int(input("Количество элементов : "))
for i in range(0, n):
    el = int(input("Введите элемент: "  ))
    lst.append(el)
print(lst)
if len(lst) % 2 == 0:
    i = 0
    while i < len(lst):
        p = lst[i]
        lst[i] = lst[i+1]
        lst[i+1] = p
        i += 2
else:
    i = 0
    while i < len(lst) - 1:
        p = lst[i]
        lst[i] = lst[i + 1]
        lst[i + 1] = p
        i += 2
print(lst)