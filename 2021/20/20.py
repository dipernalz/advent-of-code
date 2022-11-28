inpt = open('input.txt', 'r').read().rstrip().split('\n\n')

key = inpt[0].replace('#', '1').replace('.', '0')
temp = [i.replace('#', '1').replace('.', '0') for i in inpt[1].split('\n')]
m, n = len(temp), len(temp[0])
grid = {(r, c): int(temp[r][c]) for r in range(m) for c in range(n)}


def enhance(g, repeats):
    for i in range(1, repeats + 1):
        nxt = {}
        for r in range(-i, m + i):
            for c in range(-i, n + i):
                b = ''
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        if (r + dr, c + dc) not in g:
                            b += key[0] if i % 2 == 0 else key[-1]
                        else:
                            b += str(g[(r + dr, c + dc)])
                nxt[(r, c)] = int(key[int(b, 2)])
        g = nxt
    return g


# Part 1
print(sum(enhance(grid, 2).values()))

# Part 2
print(sum(enhance(grid, 50).values()))
