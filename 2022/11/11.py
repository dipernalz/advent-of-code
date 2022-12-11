#!/usr/bin/env python3

# 356/1012

from collections import deque
import re

inpt = [
    m.split("\n")
    for m in open("input.txt", "r").read().strip().split("\n\n")
]
n = len(inpt)
op = [
    lambda x: x * 11,
    lambda x: x + 1,
    lambda x: x + 7,
    lambda x: x + 3,
    lambda x: x * x,
    lambda x: x + 4,
    lambda x: x * 5,
    lambda x: x + 8,
]

test = [int(re.search(r"\d+", m[3]).group()) for m in inpt]
throw = [list(map(int, re.findall(r"\d+", m[4] + m[5]))) for m in inpt]

# Part 1
items = [
    deque(map(int, re.findall(r"\d+", m[1])))
    for m in inpt
]

c = [0] * n
for r in range(20):
    for m in range(n):
        c[m] += len(items[m])
        while items[m]:
            v = op[m](items[m].popleft()) // 3
            items[throw[m][min(v % test[m], 1)]].append(v)

c.sort()
print(c[-1] * c[-2])

# Part 2
items = [
    deque(
        list(map(lambda t: i % t, test))
        for i in map(int, re.findall(r"\d+", m[1]))
    )
    for m in inpt
]

c = [0] * n
for _ in range(10000):
    for m in range(n):
        c[m] += len(items[m])
        while items[m]:
            v = [op[m](w) % test[i] for i, w in enumerate(items[m].popleft())]
            items[throw[m][min(v[m], 1)]].append(v)

c.sort()
print(c[-1] * c[-2])
