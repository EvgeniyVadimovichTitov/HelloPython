# Напишите программу, которая принимает на вход число N и выдаёт
# последовательность из N членов.
# Пример:
# o	Для N = 5: 1, -3, 9, -27, 81

# N = int(input('N = '))

#a =[ (-3)**i for i in range(N)]
# print(a)
# a=[3*i+1 for i in range(1,N+1)]
# print(a)

str1 = input()
str2 = input()
count = 0
for i in str1:
    for j in str2:
        if i == j:
            count += 1
print(count)
12345
12245
