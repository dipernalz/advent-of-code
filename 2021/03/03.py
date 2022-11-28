# 1241/948

from collections import defaultdict

inpt = open('input.txt', 'r').read().rstrip().split('\n')

# Part 1
n = len(inpt[0])
x = defaultdict(int)
for i in inpt:
    for j in range(n):
        x[j] += int(i[j])

g, e = 0, 0
add = 1
for i in sorted(x, reverse=True):
    if x[i] > len(inpt) / 2:
        g += add
    else:
        e += add
    add *= 2
print(g * e)

# Part 2
oxy = inpt.copy()
i = 0
while len(oxy) > 1:
    c = sum('1' == x[i] for x in oxy)
    new_oxy = []
    if c >= len(oxy) / 2:
        for x in oxy:
            if x[i] == '1':
                new_oxy.append(x)
    else:
        for x in oxy:
            if x[i] == '0':
                new_oxy.append(x)
    oxy = new_oxy
    i += 1
o = int(oxy[0], 2)

c02 = inpt.copy()
i = 0
while len(c02) > 1:
    c = sum('1' == x[i] for x in c02)
    new_c02 = []
    if c >= len(c02) / 2:
        for x in c02:
            if x[i] == '0':
                new_c02.append(x)
    else:
        for x in c02:
            if x[i] == '1':
                new_c02.append(x)
    c02 = new_c02
    i += 1
c = int(c02[0], 2)

print(o * c)
