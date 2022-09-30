# Задайте число N, создайте список: [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции (случайные) хранятся в файле file.txt
# (создаётся во время выполнения кода и зависит от количества элементов в списке)
# в одной строке одно число.
# Пример:
# Файл:
# 4
# 5
# 2
# N = 3 = > [-3, -2, -1, 0, 1, 2, 3]
# Результат: 1*2*(-1) = -2

import random
n = random.randint(3, 6)

multiplication = 1


def Create_List(N):
    list = []
    for i in range(-N, N+1):
        list.append(i)
    return list


def Create_File(N):
    data = open('file.txt', 'w')
    count_line = random.randint(1, N)
    for i in range(1, count_line+1):
        # [-N,N] - интересно было поработать с отрицательными индексами, понимаю,
        # что приводит к повторам используемых элементов
        data.write(str(random.randint(-N, N)) + '\n')
    data.close()
    return data


list_n = Create_List(n)
print(list_n)
Create_File(n)
path = 'file.txt'
data = open(path, 'r')
for line in data:
    i = int(line)
    multiplication *= int(list_n[i])
data.close()
print('Произведение элементов списка с индексакми, \nуказанными в файле, равно:', multiplication)
