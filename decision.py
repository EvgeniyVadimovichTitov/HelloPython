# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# o[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random
users_nums = []
count = 1
#sum = 0
for i in range(1, random.randint(3, 9)):
    users_nums.append(random.randint(-10, 9))
print(users_nums, end=' -> ')
# while count < len(list):
#     sum += int(list[count])
#     count += 2
# print(sum)
print(f'Sum => {sum(users_nums[1::2])}')
