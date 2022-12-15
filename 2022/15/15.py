#!/usr/bin/env python3

import re

inpt = [
    tuple(map(int, re.findall(r"-?\d+", s)))
    for s in open("input.txt", "r").read().strip().split("\n")
]


def get_intervals(row):
    intervals = []
    for sx, sy, bx, by in inpt:
        d = abs(sx - bx) + abs(sy - by)
        if abs(row - sy) < d:
            t = d - abs(row - sy)
            intervals.append([sx - t, sx + t])
    intervals.sort()
    i = 0
    while i + 1 < len(intervals):
        if intervals[i][1] >= intervals[i + 1][0]:
            intervals[i][1] = max(intervals[i][1], intervals[i + 1][1])
            intervals.pop(i + 1)
        else:
            i += 1
    return intervals


# Part 1
row = 2000000
intervals = get_intervals(row)
row_beacons = set(bx for _, _, bx, by in inpt if by == row)
print(sum(
    b - a + 1 - (1 if any(a <= bx <= b for bx in row_beacons) else 0)
    for a, b in intervals
))

# Part 2
max_row = 4000000
for row in range(max_row):
    intervals = get_intervals(row)
    if len(intervals) == 2:
        print((intervals[0][1] + 1) * max_row + row)
        break
