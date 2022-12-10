#!/usr/bin/env python3

inpt = open("input.txt", "r").read().strip().split("\n")

m, n = 6, 40

p = 0
result = ""
register = [1]
for l in inpt:
    result += "#" if abs(register[-1] - p) <= 1 else "."
    p = (p + 1) % n
    register.append(register[-1])
    if l[0] == "a":
        result += "#" if abs(register[-1] - p) <= 1 else "."
        p = (p + 1) % n
        register.append(register[-1] + int(l.split()[1]))

# Part 1
print(sum(register[i - 1] * i for i in range(20, 260, n)))

# Part 2
for r in range(m):
    for c in range(n):
        print(result[r * n + c], end="")
    print()
