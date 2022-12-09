#!/usr/bin/env python3

inpt = open('input.txt', 'r').read().strip().split('\n')
scores = {"X": 1, "Y": 2, "Z": 3}

# Part 1
s = 0
for i in inpt:
    a, b = i.split()
    s += scores[b]
    if a == "A" and b == "Y":
        s += 6
    if a == "B" and b == "Z":
        s += 6
    if a == "C" and b == "X":
        s += 6
    if ["A", "B", "C"].index(a) == ["X", "Y", "Z"].index(b):
        s += 3
print(s)

# Part 2
s = 0
for i in inpt:
    a, b = i.split()
    b = "XYZ"[
        ("ABC".index(a) + 3 - (1 if b == "X" else 0 if b == "Y" else 2)) % 3
    ]
    s += scores[b]
    if a == "A" and b == "Y":
        s += 6
    if a == "B" and b == "Z":
        s += 6
    if a == "C" and b == "X":
        s += 6
    if ["A", "B", "C"].index(a) == ["X", "Y", "Z"].index(b):
        s += 3
print(s)
