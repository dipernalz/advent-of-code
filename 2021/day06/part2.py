# 5574 (lol)

from collections import Counter, defaultdict

curr = Counter(list(map(int, open('input.txt', 'r').read().split(','))))

for i in range(256):
    nxt = defaultdict(int)
    for j in range(9):
        if j == 0:
            nxt[8] += curr[j]
            nxt[6] += curr[j]
        else:
            nxt[j - 1] += curr[j]
    curr = nxt
print(sum(curr.values()))
