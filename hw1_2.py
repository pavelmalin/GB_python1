''' 
Задача №2
По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b,
проходящей через эти точки.
'''

x1 = int(input('Введите x1: '))
x2 = int(input('Введите x2: '))
y1 = int(input('Введите y1: '))
y2 = int(input('Введите y2: '))

k = (y1-y2)/(x1-x2)
b = y2-(k*x2)

print(f'Уравнение прямой: y = (%s)x + (%s)'%(k,b))