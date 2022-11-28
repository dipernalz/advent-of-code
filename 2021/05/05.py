# 172/111

from collections import defaultdict

inpt = open('input.txt', 'r').read().rstrip().split('\n')
inpt = [[list(map(int, j.split(','))) for j in i.split(' -> ')] for i in inpt]

# Part 1
counter = defaultdict(int)
for a, b in inpt:
    x1, y1 = a
    x2, y2 = b
    if x1 == x2:
        if y1 < y2:
            for i in range(y1, y2 + 1):
                counter[(x1, i)] += 1
        else:
            for i in range(y2, y1 + 1):
                counter[(x1, i)] += 1
    elif y1 == y2:
        if x1 < x2:
            for i in range(x1, x2 + 1):
                counter[(i, y1)] += 1
        else:
            for i in range(x2, x1 + 1):
                counter[(i, y1)] += 1

print(sum(1 for x in counter if counter[x] >= 2))

# Part 2
counter = defaultdict(int)
for a, b in inpt:
    x1, y1 = a
    x2, y2 = b
    if x1 == x2:
        if y1 < y2:
            for i in range(y1, y2 + 1):
                counter[(x1, i)] += 1
        else:
            for i in range(y2, y1 + 1):
                counter[(x1, i)] += 1
    elif y1 == y2:
        if x1 < x2:
            for i in range(x1, x2 + 1):
                counter[(i, y1)] += 1
        else:
            for i in range(x2, x1 + 1):
                counter[(i, y1)] += 1
    else:
        dx = -1 if x2 < x1 else 1
        dy = -1 if y2 < y1 else 1
        counter[(x1, y1)] += 1
        while x1 != x2:
            x1 += dx
            y1 += dy
            counter[(x1, y1)] += 1

print(sum(1 for x in counter if counter[x] >= 2))
