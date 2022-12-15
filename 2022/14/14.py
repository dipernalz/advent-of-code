#!/usr/bin/env python3

from collections import Counter, defaultdict, deque
from functools import cache
from heapq import *
from itertools import combinations, permutations, product
import math
import re

inpt = open("input.txt", "r").read().strip().split("\n")

rock = set()
for t in inpt:
    paths = [tuple(map(int, p.split(",")))for p in t.split(" -> ")]
    cx, cy = paths[0]
    for nx, ny in paths[1:]:
        if nx == cx:
            for y in range(min(ny, cy), max(ny, cy) + 1):
                rock.add((cx, y))
        else:
            for x in range(min(nx, cx), max(nx, cx) + 1):
                rock.add((x, cy))
        cx, cy = nx, ny
max_y = max(y for _, y in rock)
start = 500, 0

# Part 1
filled = rock.copy()
stopped = True
while stopped:
    x, y = start
    stopped = False
    while y <= max_y:
        if (x, y + 1) not in filled:
            x, y = x, y + 1
        elif (x - 1, y + 1) not in filled:
            x, y = x - 1, y + 1
        elif (x + 1, y + 1) not in filled:
            x, y = x + 1, y + 1
        else:
            stopped = True
            filled.add((x, y))
            break
print(len(filled) - len(rock))

# Part 2
filled = rock.copy()
while start not in filled:
    x, y = start
    while (x, y) not in filled:
        if y == max_y + 1:
            filled.add((x, y))
        elif (x, y + 1) not in filled:
            x, y = x, y + 1
        elif (x - 1, y + 1) not in filled:
            x, y = x - 1, y + 1
        elif (x + 1, y + 1) not in filled:
            x, y = x + 1, y + 1
        else:
            filled.add((x, y))
print(len(filled) - len(rock))
