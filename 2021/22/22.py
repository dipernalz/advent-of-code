from collections import defaultdict
import re

inpt = open('input.txt', 'r').read().rstrip().split('\n')

instr, ops = [], []
for i in inpt:
    x0, x1, y0, y1, z0, z1 = map(int, re.findall(r'-?\d+', i))
    instr.append(((x0, x1), (y0, y1), (z0, z1)))
    ops.append(True if i[:2] == 'on' else False)
n = len(instr)

# Part 1
state = set()
for i in range(n):
    x0, x1, y0, y1, z0, z1 = instr[i][0] + instr[i][1] + instr[i][2]
    for x in range(max(x0, -50), min(x1 + 1, 51)):
        for y in range(max(y0, -50), min(y1 + 1, 51)):
            for z in range(max(z0, -50), min(z1 + 1, 51)):
                if ops[i]:
                    state.add((x, y, z))
                elif (x, y, z) in state:
                    state.remove((x, y, z))
print(len(state))


# Part 2
def volume(c):
    v = 1
    for x0, x1 in c:
        if x1 < x0:
            return 0
        v *= x1 - x0 + 1
    return v


def intersection(c0, c1):
    c = tuple((max(c0[i][0], c1[i][0]), min(c0[i][1], c1[i][1]))
              for i in range(3))
    return c if volume(c) else None


cubes = defaultdict(int)
for i in range(n):
    nxt = defaultdict(int)
    nxt[instr[i]] += ops[i]
    for cube, sign in cubes.items():
        intersect = intersection(instr[i], cube)
        if intersect:
            nxt[intersect] += cubes[cube] * -1
    for cube in nxt:
        cubes[cube] += nxt[cube]
        if cubes[cube] == 0:
            del cubes[cube]
print(sum(volume(cube) * sign for cube, sign in cubes.items()))
