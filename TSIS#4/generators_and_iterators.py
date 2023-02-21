#1
n = int(input())
a = (i**2 for i in range(1, 1000000000000000000000000))
for i in a:
    if i <= n:
        print(i)
    else:
        break

#2.Напишите программу с использованием генератора для печати четных 
# чисел от 0 до n в форме, разделенной запятыми, где n вводится с консоли.
n =int(input())
l = []
a = (i for i in range(1, n + 1))
for i in a:
    if i % 2 == 0:
        l.append(i)
print(*l, sep = ', ')

#3.Определите функцию с генератором, которая может перебирать числа, кратные 3 и 4, в заданном диапазоне от 0 до n.
def divisible(a):
    for i in a:
        if i % 3 == 0 and i % 4 == 0:
            print(i)
n = int(input())
a =(i for i in range(1, n))
divisible(a)


#4
'''
Реализуйте генератор квадратов для получения квадрата всех чисел от (a) до (b). 
Протестируйте его с помощью цикла "for" и выведите каждое из полученных значений.
'''
import math
a = int(input())
b = int(input())
x = int(math.sqrt(a))
y = int(math.sqrt(b))
g = (i**2 for i in range(x, y + 1))
for i in g:
    print(i)

#5
n = int(input())
d =  (i for i in range(n, 0, -1))
for i in d:
    print(i)
