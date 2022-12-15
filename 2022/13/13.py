#!/usr/bin/env python3

from functools import cmp_to_key
from itertools import chain

inpt = [
    list(map(eval, p.split("\n")))
    for p in open("input.txt", "r").read().strip().split("\n\n")
]


def compare(a, b):
    for i in range(max(len(a), len(b))):
        if i == len(a) or i == len(b):
            return len(a) - len(b)
        if isinstance(a[i], int) and isinstance(b[i], int):
            if a[i] != b[i]:
                return a[i] - b[i]
            continue
        change_a, change_b = False, False
        if (
            isinstance(a[i], list) and isinstance(b[i], int) or
            isinstance(a[i], int) and isinstance(b[i], list)
        ):
            if isinstance(a[i], int):
                change_a = True
                a[i] = [a[i]]
            if isinstance(b[i], int):
                change_b = True
                b[i] = [b[i]]
        r = compare(a[i], b[i])
        if change_a:
            a[i] = a[i][0]
        if change_b:
            b[i] = b[i][0]
        if r != 0:
            return r
    return 0


# Part 1
s = 0
for i, (a, b) in enumerate(inpt):
    if compare(a, b) < 0:
        s += i + 1
print(s)

# Part 2
d1, d2 = [[2]], [[6]]
inpt = list(chain.from_iterable(inpt)) + [d1, d2]
inpt.sort(key=cmp_to_key(compare))
print((inpt.index(d1) + 1) * (inpt.index(d2) + 1))
