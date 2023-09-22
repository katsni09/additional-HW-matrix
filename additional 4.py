# - ввести з клавіатури порядковий номер одного стовпця
# і потім іншого стовпця і поміняти їх місцями в матрицю (аналогічно зробити з рядком)
from random import *
n = 10
a = [[0] * n for i in range(n)]
row1 = int(input())
row2 = int(input())

for i in range(n):
    for j in range(n):
        a [i] [j] = randint(10,99)
for row in a:
    print(' '.join([str(elem) for elem in row]))

a [row1],a[row2]= a[row2],a[row1]

print()

for row in a:
    print(' '.join([str(elem) for elem in row]))