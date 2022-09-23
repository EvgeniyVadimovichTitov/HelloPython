##Напишите программу для. проверки истинности утверждения 
##¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
print('значения х, у и z могут быть истиной или ложью (1 или 0)')
x = bool(input('x = '))
y = bool(input('y = '))
z = bool(input('z = '))

print(not(x or y or z) == (not x and not y and not z))