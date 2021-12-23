from collections import defaultdict

inpt = open('input.txt', 'r').read().replace('\n', '')
n = int(len(inpt) ** .5)

# Part 1
curr = inpt
visited = set()
while True:
    if curr in visited:
        break
    visited.add(curr)
    nxt = ''
    for i, c in enumerate(curr):
        nbrs = ((1 if i % n != 0 and curr[i - 1] == '#' else 0) +
                (1 if i % n != n - 1 and curr[i + 1] == '#' else 0) +
                (1 if i // n != 0 and curr[i - n] == '#' else 0) +
                (1 if i // n != n - 1 and curr[i + n] == '#' else 0))
        nxt += '#' if nbrs == 1 else '#' if c == '.' and nbrs == 2 else '.'
    curr = nxt
print(sum(2 ** i for i, c in enumerate(curr) if c == '#'))

# Part 2
mid = n ** 2 // 2
blank = '.' * mid + '?' + '.' * mid
grids = defaultdict(lambda: blank)
grids[0] = inpt[:mid] + '?' + inpt[mid + 1:]
for i in range(1, 200 + 1):
    nxt_grids = defaultdict(lambda: blank)
    for layer in range(-i, i + 1):
        nxt = ''
        for j in range(n * n):
            nbrs = 0
            if j == mid:
                nxt += '?'
                continue
            if j % n != 0:
                nbrs += 1 if grids[layer][j - 1] == '#' else 0
                if grids[layer][j - 1] == '?':
                    nbrs += sum(1 for l in range(0, n ** 2, n)
                                if grids[layer - 1][l + n - 1] == '#')
            else:
                nbrs += 1 if grids[layer + 1][mid - 1] == '#' else 0
            if j % n != n - 1:
                nbrs += 1 if grids[layer][j + 1] == '#' else 0
                if grids[layer][j + 1] == '?':
                    nbrs += sum(1 for l in range(0, n ** 2, n)
                                if grids[layer - 1][l] == '#')
            else:
                nbrs += 1 if grids[layer + 1][mid + 1] == '#' else 0
            if j // n != 0:
                nbrs += 1 if grids[layer][j - n] == '#' else 0
                if grids[layer][j - n] == '?':
                    nbrs += sum(1 for l in range(0, n) if
                                grids[layer - 1][l + n ** 2 - n] == '#')
            else:
                nbrs += 1 if grids[layer + 1][mid - n] == '#' else 0
            if j // n != n - 1:
                nbrs += 1 if grids[layer][j + n] == '#' else 0
                if grids[layer][j + n] == '?':
                    nbrs += sum(1 for l in range(0, n)
                                if grids[layer - 1][l] == '#')
            else:
                nbrs += 1 if grids[layer + 1][mid + n] == '#' else 0
            nxt += '#' if nbrs == 1 else '#' if grids[layer][j] == '.' and \
                                                nbrs == 2 else '.'
        nxt_grids[layer] = nxt
    grids = nxt_grids
print(sum(grids[i].count('#') for i in grids))
