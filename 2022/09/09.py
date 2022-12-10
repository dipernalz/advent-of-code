#!/usr/bin/env python3

inpt = [
    i.split()
    for i in open("input.txt", "r").read().strip().split("\n")
]

directions = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, 1),
    "D": (0, -1),
}

def f(r):
    x = [0] * r
    y = [0] * r
    visited = set()
    for m in inpt:
        d = m[0]
        n = int(m[1])
        dx, dy = directions[d]
        for i in range(n):
            x[0] += dx
            y[0] += dy
            for i in range(1, r):
                a = x[i - 1] - x[i]
                b = y[i - 1] - y[i]
                if abs(a) + abs(b) > 1 and not (abs(a) == 1 and abs(b) == 1):
                    x[i] += -1 if a < 0 else 1 if a > 0 else 0
                    y[i] += -1 if b < 0 else 1 if b > 0 else 0
            visited.add((x[-1], y[-1]))
    return len(visited)

# Part 1
print(f(2))

# Part 2
print(f(10))
