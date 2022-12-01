#!/usr/bin/env python3

# 471/222

inpt = [x.split('\n')
        for x in open('input.txt', 'r').read().strip().split('\n\n')]

# Part 1
print(max(sum([int(y) for y in x]) for x in inpt))

# Part 2
print(sum(sorted(sum([int(y) for y in x]) for x in inpt)[-3:]))
