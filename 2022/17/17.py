#!/usr/bin/env python3

# 276/683

inpt = open("input.txt", "r").read().strip()
rocks = {
    0: [(0, 0), (1, 0), (2, 0), (3, 0)],
    1: [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],
    2: [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
    3: [(0, 0), (0, 1), (0, 2), (0, 3)],
    4: [(0, 0), (0, 1), (1, 0), (1, 1)],
}
w = 7

i = 0
k = None
max_y = [0]
filled = set()
g = 1000000000000
repeat_start, repeat_end = None, None
for j in range(g):
    r = [(x + 2, y + max_y[-1] + 4) for x, y in rocks[j % len(rocks)]]
    while True:
        if (
            inpt[i] == "<" and
            all(x >= 1 and (x - 1, y) not in filled for x, y in r)
        ):
            r = [(x - 1, y) for x, y in r]
        elif (
            inpt[i] == ">" and
            all(x < w - 1 and (x + 1, y) not in filled for x, y in r)
        ):
            r = [(x + 1, y) for x, y in r]
        i = (i + 1) % len(inpt)
        if any(y == 1 or (x, y - 1) in filled for x, y in r):
            break
        r = [(x, y - 1) for x, y in r]
    max_y.append(max([y for _, y in r] + [max_y[-1]]))
    filled.update(r)
    if k is None and all((x, max_y[-1]) in filled for x in range(w)):
        repeat_start = j
        k = i
    elif k == i and all((x, max_y[-1]) in filled for x in range(w)):
        repeat_end = j
        break

# Part 1
print(max_y[2022])

# Part 2
interval_length = repeat_end - repeat_start
interval_height = max_y[repeat_end] - max_y[repeat_start]
print(
    (g - repeat_start) // interval_length * interval_height +
    max_y[repeat_start + (g - repeat_start) % interval_length]
)
