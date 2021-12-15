# 122/99

inpt = open('input.txt', 'r').read().rstrip().split('\n')
grid = [list(map(int, l)) for l in inpt]

m, n = len(grid), len(grid[0])

total = 0
for i in range(1, 10 ** 6):
    for r in range(m):
        for c in range(n):
            grid[r][c] += 1

    flashed = set()
    flash = True
    while flash:
        flash = False
        for r in range(m):
            for c in range(n):
                if grid[r][c] > 9 and (r, c) not in flashed:
                    flashed.add((r, c))
                    total += 1
                    flash = True
                    for dr in (-1, 0, 1):
                        for dc in (-1, 0, 1):
                            if dr == 0 and dc == 0:
                                continue
                            if 0 <= r + dr < m and 0 <= c + dc < n:
                                grid[r + dr][c + dc] += 1

    if i == 100:
        print(total)
    if len(flashed) == m * n:
        print(i)
        break
    for r, c in flashed:
        grid[r][c] = 0
