# 1241

from collections import defaultdict

inpt = open('input.txt', 'r').read().rstrip().split('\n')

n = len(inpt[0])
x = defaultdict(int)
for i in inpt:
    for j in range(n):
        x[j] += int(i[j])

g, e = 0, 0
add = 1
for i in sorted(x, reverse=True):
    if x[i] > len(inpt) / 2:
        g += add
    else:
        e += add
    add *= 2
print(g*e)
