#!/usr/bin/env python3

from collections import defaultdict, deque
from functools import cache
import re

inpt = open("input.txt", "r").read().strip().split("\n")
start = "AA"

graph = {}
rate = {}
for i in inpt:
    m = re.match(r"^.*([A-Z]{2}).*?(\d+).*?([A-Z]{2}.*?)$", i)
    graph[m.group(1)] = m.group(3).split(", ")
    rate[m.group(1)] = int(m.group(2))

id = {v: 1 << i for i, v in enumerate(sorted([k for k in graph if rate[k]]))}

dist = defaultdict(dict)
for n in graph:
    if n == start or rate[n]:
        v = set()
        q = deque([(n, 0)])
        while q:
            c, d = q.popleft()
            if c in v:
                continue
            v.add(c)
            if n != c and rate[c]:
                dist[n][c] = d
            for nbr in graph[c]:
                if nbr not in v:
                    q.append((nbr, d + 1))

# Part 1
@cache
def search1(a, t, v):
    s = 0
    for nbr, d in dist[a].items():
        nt = t - d - 1
        if not v & id[nbr] and nt > 0:
            s = max(s, nt * rate[nbr] + search1(nbr, nt, v | id[nbr]))
    return s
print(search1(start, 30, 0))

# Part 2
@cache
def search2(a, at, b, bt, v):
    s = 0
    for nbr, d in dist[a].items():
        nt = at - d - 1
        if not v & id[nbr] and nt > 0:
            s = max(s, nt * rate[nbr] + search2(nbr, nt, b, bt, v | id[nbr]))
    for nbr, d in dist[b].items():
        nt = bt - d - 1
        if not v & id[nbr] and nt > 0:
            s = max(s, nt * rate[nbr] + search2(a, at, nbr, nt, v | id[nbr]))
    return s
print(search2(start, 26, start, 26, 0))
