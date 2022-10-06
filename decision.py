# Задайте натуральное число N. Напишите программу, которая
# составит список простых множителей числа N.
# 70 = 2*5*7 = > [2, 5, 7]
# 140 = 2*2*5*7 = > [2, 2, 5, 7]
# 140 | 2
# 70 | 2
# 35 | 5
# 7 | 7
import random
num = random.randint(1, 1000)


def find_den(n, i=2):
    li = []
    while n >= i:
        if n % i == 0:
            li.append(i)
            n = n/i
            i = 2
        else:
            i += 1
    return li


print(num, '=>', find_den(num))
