'''
Задача №6
Определить, является ли год, который ввел пользователь, високосным или невисокосным.
'''

years = int(input('Введите год: '))

C = years%4
B = years%100
D = years%400
if C == 0 and D == 0:
  print('Високосный')
elif C == 0 and B != 0 and D != 0:
  print('Високосный')
else:
  print('Невисокосный')