# 779

inpt = open('input.txt', 'r').read().rstrip().split('\n')
grid = [[int(i) for i in l] for l in inpt]

m, n = len(grid), len(grid[0])
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

basins = []
for r in range(m):
    for c in range(n):
        if grid[r][c] == 9:
            continue
        size = 0
        q = [(r, c)]
        while q:
            x, y = q.pop()
            if grid[x][y] == 9:
                continue
            size += 1
            grid[x][y] = 9
            for dc, dr in d:
                if 0 <= x + dr < m and 0 <= y + dc < n:
                    q.append((x + dr, y + dc))
        basins.append(size)
basins = sorted(basins)
print(basins[-1] * basins[-2] * basins[-3])
