# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
import math
import random
n = random.randint(1, 5)
print(n)
list_one_to_n = []
count = 1
while count <= n:
    list_one_to_n.append(math.factorial(count))
    count += 1
print(list_one_to_n)
