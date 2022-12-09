#!/usr/bin/env python3

import re
from string import ascii_uppercase

start, instr = open('input.txt', 'r').read().split('\n\n')
start = start.split("\n")
instr = instr.strip().split("\n")

stacks = [[] for _ in range(10)]
idx = [i for i, c in enumerate(start[5]) if c in ascii_uppercase]
for _, l in enumerate(start[:8]):
    for j, c in enumerate(l):
        if c in ascii_uppercase:
            stacks[idx.index(j) + 1].insert(0, c)

# Part 1
stacks1 = [s.copy() for s in stacks]
for i in instr:
    x, y, z = map(int, re.findall(r".*?(\d+).*?(\d+).*?(\d+)", i)[0])
    for j in range(x):
        stacks1[z].append(stacks1[y].pop())
print("".join(s[-1] for s in stacks1 if s))

# Part 2
stacks2 = [s.copy() for s in stacks]
for i in instr:
    x, y, z = map(int, re.findall(r".*?(\d+).*?(\d+).*?(\d+)", i)[0])
    stacks2[z] += stacks2[y][-x:]
    stacks2[y] = stacks2[y][:-x]
print("".join(s[-1] for s in stacks2 if s))
