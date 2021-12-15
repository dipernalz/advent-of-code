# 86/2249

inpt = open('input.txt', 'r').read().rstrip().split('\n\n')

pts = set()
for i in inpt[0].split('\n'):
    x, y = i.split(',')
    pts.add((int(x), int(y)))

# Part 1
n = 655
new_pts = pts.copy()
for x, y in pts:
    if x < n:
        new_pts.add((2 * n - x, y))

c = 0
for x, y in new_pts:
    if x > n:
        c += 1
print(c)

# Part 2
for i in inpt[1].split('\n'):
    i = i.split('=')
    f, n = i[0][-1], int(i[1])

    new_pts = set()
    if f == 'x':
        for x, y in pts:
            if x < n:
                new_pts.add((n - x - 1, y))
            elif x > n:
                new_pts.add((x - n - 1, y))
    else:
        for x, y in pts:
            if y < n:
                new_pts.add((x, y))
            elif y > n:
                new_pts.add((x, 2 * n - y))
    pts = new_pts

for y in range(max(y for x, y in pts) + 1):
    for x in range(max(x for x, y in pts), -1, -1):
        if (x, y) in pts:
            print('X', end=' ')
        else:
            print(' ', end=' ')
    print()
