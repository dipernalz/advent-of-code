#!/usr/bin/env python3

inpt = open('input.txt', 'r').read().strip().split('\n')

# Part 1
s = 0
for i in inpt:
    a, b = i.split(",")
    c, d = list(map(int, a.split("-")))
    e, f = list(map(int, b.split("-")))
    s += (c <= e and d >= f) or (e <= c and f >= d)
print(s)

# Part 2
s = 0
for i in inpt:
    a, b = i.split(",")
    c, d = list(map(int, a.split("-")))
    e, f = list(map(int, b.split("-")))
    s += (c <= e and d >= e) or (e <= c and f >= c)
print(s)
