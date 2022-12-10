#!/usr/bin/env python3

from functools import cache


class File:
    def __init__(self, size):
        self.size = size


class Dir:
    def __init__(self, parent=None):
        self.parent = parent
        self.children = {}

    @cache
    def get_size(self):
        s = 0
        for c in self.children.values():
            if isinstance(c, File):
                s += c.size
            else:
                s += c.get_size()
        return s


inpt = open("input.txt", "r").read().strip().split("\n")

root = Dir()
current = root
i = 1
while i < len(inpt):
    line = inpt[i]
    cmd = line[2:4]
    if cmd == "ls":
        i += 1
        while i < len(inpt) and inpt[i][0] != "$":
            t, name = inpt[i].split()
            current.children[name] = (
                Dir(current) if t == "dir" else File(int(t))
            )
            i += 1
    else:
        name = line[5:]
        current = current.parent if name == ".." else current.children[name]
        i += 1

ans = 0
q = [root]
sizes = []
while q:
    current = q.pop()
    ans += current.get_size() if current.get_size() <= 100000 else 0
    sizes.append(current.get_size())
    for c in current.children.values():
        if isinstance(c, Dir):
            q.append(c)

# Part 1
print(ans)

# Part 2
sizes.sort()
available_space = 70000000 - root.get_size()
for s in sizes:
    if available_space + s >= 30000000:
        print(s)
        break
