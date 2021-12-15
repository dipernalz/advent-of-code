# 334/830

inpt = open('input.txt', 'r').read().rstrip().split('\n')
inpt = [i.split() for i in inpt]

# Part 1
h, v = 0, 0
for i, j in inpt:
    if i == 'forward':
        h += int(j)
    elif i == 'up':
        v += int(j)
    else:
        v -= int(j)
print(-h*v)

# Part 2
h, v, a = 0, 0, 0
for i, j in inpt:
    if i == 'forward':
        h += int(j)
        v -= int(j) * a
    elif i == 'up':
        a -= int(j)
    else:
        a += int(j)
print(-h*v)
