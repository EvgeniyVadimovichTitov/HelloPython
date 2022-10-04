# Задайте число.
# Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.
# Пример:
# o для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
import random
import function
list_fibonachi = []
n = random.randint(8, 9)
print('Для числа', n, 'список:')
for i in range(-n, n+1):
    list_fibonachi.append(function.Fibonachi(i))
print(list_fibonachi)
