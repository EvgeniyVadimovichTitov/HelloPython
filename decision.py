# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением
# дробной части элементов.
# Пример:
# o [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
import math
lst = []
# min = 1
# max = 0

for i in range(0, random.randint(5, 10)):
    lst.append(round(random.uniform(1, 11), 2))
# for i in lst:
#     if i % 1 > max:
#         max = i % 1
#     if i % 1 < min:
#         min = i % 1
# print(lst, round((max-min), 2), sep=' => ')
print(lst, end=' => ')
lst = [round(val % 1, 2) for val in lst]

print(round((max(lst) - min(lst)), 2))
