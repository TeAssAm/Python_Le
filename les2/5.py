a = int(input("Ваше число: "))
lst = [99, 13, 8, 1, 0 ]
c = lst.count(a)
for element in lst:
    if c > 0:
        i = lst.index(a)
        lst.insert(i+c, a)
        break
    else:
        if a > element:
            j = lst.index(element)
            lst.insert(j, a)
            break
        elif a < lst[len(lst) - 1]:
            lst.append(a)
print(lst)