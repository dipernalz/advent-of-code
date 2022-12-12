#!/usr/bin/env python3

# 287/328

from collections import deque

inpt = open("input.txt", "r").read().strip().split("\n")
m, n = len(inpt), len(inpt[0])

start, end = None, None
for r in range(m):
    if "S" in inpt[r]:
        start = (r, inpt[r].index("S"))
        inpt[r] = inpt[r].replace("S", "a")
    if "E" in inpt[r]:
        end = (r, inpt[r].index("E"))
        inpt[r] = inpt[r].replace("E", "z")


def search(row, col):
    v = set()
    q = deque([(0, row, col)])
    while q:
        d, r, c = q.popleft()
        if (r, c) == end:
            return d
        if (r, c) in v:
            continue
        v.add((r, c))
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if (
                    abs(dr) == abs(dc) or
                    not 0 <= r + dr < m or
                    not 0 <= c + dc < n or
                    (r + dr, c + dc) in v or
                    ord(inpt[r + dr][c + dc]) - ord(inpt[r][c]) > 1
                ):
                    continue
                q.append((d + 1, r + dr, c + dc))
    return float("inf")


# Part 1
print(search(*start))

# Part 2
s = float("inf")
for r in range(m):
    for c in range(n):
        if inpt[r][c] == "a":
            s = min(s, search(r, c))
print(s)
