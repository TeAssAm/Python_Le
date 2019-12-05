var1 = int(input("Введите число секунд: "))
h = var1//3600
m = (var1//60)%60
s = var1%60
print("%02i:%02i:%02i" % (h,m,s))