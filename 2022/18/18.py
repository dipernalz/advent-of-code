#!/usr/bin/env python3

# 140/206

from collections import deque

inpt = set(
    tuple(map(int, i.split(",")))
    for i in open("input.txt", "r").read().strip().split("\n")
)

dp = [
    (-1, 0, 0),
    ( 1, 0, 0),
    ( 0,-1, 0),
    ( 0, 1, 0),
    ( 0, 0,-1),
    ( 0, 0, 1),
]

# Part 1
print(sum(
    (x + dx, y + dy, z + dz) not in inpt
    for x, y, z in inpt
    for dx, dy, dz in dp
))

# Part 2
s = 0
memo = {}
for x, y, z in inpt:
    for dx, dy, dz in dp:
        a = (x + dx, y + dy, z + dz)
        if a in inpt:
            continue
        v = set()
        ext = False
        q = deque([a])
        while q:
            a = q.popleft()
            if a in v:
                continue
            v.add(a)
            if a == (0, 0, 0):
                ext = True
                break
            if a in memo:
                ext = memo[a]
                break
            for d in dp:
                b = tuple(a[i] + d[i] for i in range(3))
                if b not in v and b not in inpt:
                    q.append(b)
        for a in v:
            memo[a] = ext
        s += ext
print(s)
