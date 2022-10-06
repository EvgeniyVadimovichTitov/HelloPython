# Вычислить число π c заданной точностью d
# Пример:
# при d = 0.001,π = 3.141 10^(-1)≤d≤10^(-10)

import math
import Metod_inition_d
user_answer = input(
    'Хотите задать точность числа пи? (если нет точность задается рандомно)\n')
d = Metod_inition_d.initoin_d(user_answer)
count = 0
p = ''
for i in str(math.pi):
    if (count < len(d)):
        p += i
    count += 1
print(p)
