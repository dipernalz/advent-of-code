#!/usr/bin/env python3

from collections import defaultdict

inpt = [
    list(map(int, i)) for i in open("input.txt", "r").read().strip().split("\n")
]

n = len(inpt)

visible = set()
visibility = defaultdict(lambda: 1)

max_col = [defaultdict(int) for _ in range(n)]
for r in range(n):
    max_row = defaultdict(int)
    for c in range(n):
        v = inpt[r][c]
        if v not in max_row or v not in max_col[c]:
            visible.add((r, c))
        visibility[(r, c)] *= (c - max_row[v]) * (r - max_col[c][v])
        for i in range(0, v + 1):
            max_row[i] = c
            max_col[c][i] = r

max_col = [defaultdict(lambda: n - 1) for _ in range(n)]
for r in range(n - 1, -1, -1):
    max_row = defaultdict(lambda: n - 1)
    for c in range(n - 1, -1, -1):
        v = inpt[r][c]
        if v not in max_row or v not in max_col[c]:
            visible.add((r, c))
        visibility[(r, c)] *= (max_row[v] - c) * (max_col[c][v] - r)
        for i in range(0, v + 1):
            max_row[i] = c
            max_col[c][i] = r

# Part 1
print(len(visible))

# Part 2
print(max(visibility.values()))
