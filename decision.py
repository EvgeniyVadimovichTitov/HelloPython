# Задана натуральная степень k. Сформировать случайным образом
# список коэффициентов(значения от 0 до 100) многочлена и записать
# в файл многочлен степени k и приравняйте его к нулю.
# Пример:
# k = 2 = > 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# 2*x*2 + 4*x + 5 = 0
# или
# 2*x ^ 2 + 4*x + 5 = 0

import random
k = random.randint(1, 10)


def create_equation(n, string=''):
    for i in range(n, -1, -1):
        m = random.randint(0, 100)
        if i > 1 and m > 1:
            string += '+' + str(m) + 'x^' + str(i)
        elif i > 1 and m == 1:
            string += '+' + 'x^' + str(i)
        elif i == 1 and m > 1:
            string += '+' + str(m) + 'x'
        elif i == 1 and m == 1:
            string += '+' + 'x'
        elif i == 0 and m > 0:
            string += '+' + str(m) + '=0'
        elif i == 0 and m == 0:
            string += '=0'
    if string[0] == '+':
        string = string[1:]
    return string


data = open('file.txt', 'w')
data.write(create_equation(k))
data.close()
