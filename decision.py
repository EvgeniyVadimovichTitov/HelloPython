# Реализуйте алгоритм перемешивания списка.

import random
list = []
list_replay = []
n = random.randint(4, 8)


def Mix_List(List):  # перемешивание без оператора shuffle
    list_mix = []
    while len(List) > 0:
        j = random.choice(List)
        list_mix.append(j)
        List.remove(j)
    return list_mix


for i in range(1, n):
    list.append(int(-n/2 + i))
for i in range(1, n):
    list_replay.append(int(-n/2 + i))

print(n)
print(list)
random.shuffle(list)
print(list)
print(Mix_List(list_replay))
