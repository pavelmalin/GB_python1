'''
Задача №8
Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого)
'''
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if b < a and a < c or c < a and a < b:
    print("Среднее число: a =", a)
elif a < b and b < c or c < b and b < a:
    print("Среднее число: b =", b)
else:
    print("Среднее число: c =", c)