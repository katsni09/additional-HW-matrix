from random import *

n = 10
a = [[0] * n for i in range(n)]

for i in range(n):
    for j in range(n):
        a [i] [j] = randint(10,99)
max_el = a [n-1][n-1]
min_el = a [n-1][n-1]
for i in range(n):
    for j in range(n):
        if j == n-i-1:
            if a [i][j] > max_el:
                max_el = a [i][j]
            if a [i][j] < min_el:
                    min_el = a [i][j]





for row in a:
    print(' '.join([str(elem) for elem in row]))
print (min_el, max_el)