# Задайте список из n чисел последовательности
# 〖(1+1/n)〗^n и выведите на экран их сумму.
import math
import random
n = random.randint(1, 5)
print(n)
list_seqence_to_n = []
for i in range(1, n+1):
    list_seqence_to_n.append((1+1/i)**i)
print(list_seqence_to_n)
print('Сумма элементов последовательности равна:', math.fsum(list_seqence_to_n))
