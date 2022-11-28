# 1851/571

from collections import Counter
from functools import cache
from itertools import product
import re

inpt = open('input.txt', 'r').read().rstrip().split('\n')
x0 = int(re.search(r'\d+$', inpt[0]).group(0))
y0 = int(re.search(r'\d+$', inpt[1]).group(0))

# Part 1
pos = [x0, y0]
pts = [0, 0]
n, d = 0, 0
while max(pts) < 1000:
    for _ in range(3):
        d = d % 100 + 1
        pos[n % 2] += d
    pos[n % 2] = (pos[n % 2] - 1) % 10 + 1
    pts[n % 2] += pos[n % 2]
    n += 1
print(3 * n * min(pts))

# Part 2
sums = Counter(sum(p) for p in product((1, 2, 3), repeat=3))


@cache
def simulate(x, y, xp, yp, t):
    if xp >= 21:
        return 1, 0
    if yp >= 21:
        return 0, 1

    wins = (0, 0)
    for s in sums:
        if t:
            nx = (x + s - 1) % 10 + 1
            sim = simulate(nx, y, xp + nx, yp, False)
        else:
            ny = (y + s - 1) % 10 + 1
            sim = simulate(x, ny, xp, yp + ny, True)
        wins = tuple(wins[i] + sim[i] * sums[s] for i in range(2))
    return wins


print(max(simulate(x0, y0, 0, 0, True)))
