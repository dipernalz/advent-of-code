#!/usr/bin/env python3

inpt = open('input.txt', 'r').read().strip().split('\n')[0]

def f(l):
    for i in range(len(inpt)):
        if len(set(inpt[i:i + l])) == l:
            return i + l

print(f(4))
print(f(14))
