# Даны два файла, в каждом из которых находится запись многочлена,
# приравненного к нулю. Задача - сформировать файл, содержащий
# сумму многочленов(суммируем подобные слагаемые).
# Пример:
# 1 Файл: 2*x2 + 4*x + 5 = 0
# 2 Файл: 4*x2 + 7*x + 9 = 0
# 3 Файл: (содержит результат) 6*x2 + 11*x + 14 = 0
# Пример:
# 1 Файл: 2*x3 + 4*x2 + 5*x + 1 = 0
# 2 Файл: 4*x2 + 7*x + 9 = 0
# 3 Файл: (содержит результат) 2*x3 + 8*x2 + 12
def find_equation(files_name):
    data = open(files_name, 'r')
    for line in data:
        n = line[:-2]
    data.close()
    return n


x = find_equation('file1.txt').split('+')
y = find_equation('file2.txt').split('+')
print(x, y)
lst_1 = []
for i in x:
    if i.find('x') != -1:
        lst_1.append(int(i[:i.find('x')]))
    else:
        lst_1.append(int(i))
lst_2 = []
for i in y:
    if i.find('x') != -1:
        lst_2.append(int(i[:i.find('x')]))
    else:
        lst_2.append(int(i))
lst_sum = []
for i in range(0, (len(x))):
    lst_sum.append(str(lst_1[i]+lst_2[i]))
wr = ''
count = 1
for i in lst_sum[:-2]:
    wr += i+'x^' + str(len(lst_sum)-count)+'+'
    count += 1
wr += lst_sum[-2]+'x'+'+'+lst_sum[-1]+'=0'
print(wr)
data = open('file3.txt', 'w')
data.write(wr)
data.close()
