# - ввести з клавіатури порядковий номер стовпця -
# вивести цифри з цього стовпця на екран (аналогічно зробити з рядком)

from random import *

n = 10
a = [[0] * n for i in range(n)]

for i in range(n):
    for j in range(n):
        a [i] [j] = randint(10,99)
for i in range(n):
    print(i, end=" Row ")
    for j in range(n):
        print(a [i][j], end=" ")
    print()



for row in a:
    print(' '.join([str(elem) for elem in row]))
