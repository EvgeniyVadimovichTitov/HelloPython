# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# o 45 -> 101101
# o 3 -> 11
# o 2 -> 10

n = int(input('Введите целое число: '))
n_copy = n
n_second = ''
while n > 0:
    n_second = str(n % 2)+n_second
    n = n//2
print(n_copy, '=>', n_second, 'или', bin(n_copy), '(с помощью bin())')
