# 86/5574

from collections import Counter, defaultdict

# Part 1
fish = list(map(int, open('input.txt', 'r').read().split(',')))

for i in range(80):
    n = len(fish)
    for j in range(len(fish)):
        if fish[j] == 0:
            fish[j] = 6
            fish.append(8)
        else:
            fish[j] -= 1
print(len(fish))

# Part 2
fish = Counter(list(map(int, open('input.txt', 'r').read().split(','))))

for i in range(256):
    nxt = defaultdict(int)
    for j in range(9):
        if j == 0:
            nxt[8] += fish[j]
            nxt[6] += fish[j]
        else:
            nxt[j - 1] += fish[j]
    fish = nxt
print(sum(fish.values()))
