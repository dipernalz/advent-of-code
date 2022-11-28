# 310/231

import re

inpt = open('input.txt', 'r').read().rstrip().split('\n')[0]
x_low, x_high, y_low, y_high = map(int, re.findall(r'-?\d+', inpt))

y_max = -float('inf')
c = 0
for vx0 in range(-500, 500):
    for vy0 in range(-500, 500):
        vx, vy = vx0, vy0
        x, y = 0, 0
        ym = -float('inf')
        for _ in range(1000):
            if x_low <= x <= x_high and y_low <= y <= y_high:
                y_max = max(ym, y_max)
                c += 1
                break
            ym = max(ym, y)

            x += vx
            y += vy
            vx += -1 if vx > 0 else 1 if vx < 0 else 0
            vy -= 1

            if ((vx == 0 and not x_low <= x <= x_high) or
                    (vx < 0 and x < x_low) or
                    (vx > 0 and x > x_high)):
                break
            if y < y_low and vy <= 0:
                break

print(y_max)
print(c)
