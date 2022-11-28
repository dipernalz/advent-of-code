# 293/236

from collections import defaultdict
from heapq import *

inpt = open('input.txt', 'r').read().rstrip().split('\n')
grid = [list(map(int, l)) for l in inpt]

# Part 1
m, n = len(grid), len(grid[0])
distances = defaultdict(lambda: float('inf'))
q = [(0, 0, 0)]
while q:
    cost, r, c = heappop(q)
    if r == m - 1 and c == n - 1:
        print(cost)
        break
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if abs(dr) == abs(dc) or not (0 <= r + dr < m and 0 <= c + dc < n):
                continue
            new_cost = cost + grid[r + dr][c + dc]
            if new_cost < distances[(r + dr, c + dc)]:
                distances[(r + dr, c + dc)] = new_cost
                heappush(q, (new_cost, r + dr, c + dc))

# Part 2
for r in range(m):
    for _ in range(4):
        grid[r] += [i % 9 + 1 for i in grid[r][-n:]]
for _ in range(4 * m):
    grid.append([i % 9 + 1 for i in grid[-n]])

m, n = len(grid), len(grid[0])
distances = defaultdict(lambda: float('inf'))
q = [(0, 0, 0)]
while q:
    cost, r, c = heappop(q)
    if r == m - 1 and c == n - 1:
        print(cost)
        break
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if abs(dr) == abs(dc) or not (0 <= r + dr < m and 0 <= c + dc < n):
                continue
            new_cost = cost + grid[r + dr][c + dc]
            if new_cost < distances[(r + dr, c + dc)]:
                distances[(r + dr, c + dc)] = new_cost
                heappush(q, (new_cost, r + dr, c + dc))
