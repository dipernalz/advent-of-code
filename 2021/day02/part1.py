# 334

inpt = open('input.txt', 'r').read().rstrip().split('\n')
inpt = [i.split() for i in inpt]

h, v = 0, 0
for i, j in inpt:
    if i == 'forward':
        h += int(j)
    elif i == 'up':
        v += int(j)
    else:
        v -= int(j)
print(-h*v)
