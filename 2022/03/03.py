#!/usr/bin/env python3

from string import ascii_letters

inpt = open('input.txt', 'r').read().strip().split('\n')

# Part 1
s = 0
for line in inpt:
    l = len(line) // 2
    s += sum(
        ascii_letters.index(c) + 1 for c in (set(line[:l]) & set(line[l:]))
    )
print(s)

# Part 2
s = 0
for i in range(len(inpt) // 3):
    s += 1 + ascii_letters.index(
        set.intersection(*map(set, inpt[3*i:3*i+3])).pop()
    )
print(s)
