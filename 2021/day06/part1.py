# 86

curr = list(map(int, open('input.txt', 'r').read().split(',')))

for i in range(80):
    n = len(curr)
    for j in range(len(curr)):
        if curr[j] == 0:
            curr[j] = 6
            curr.append(8)
        else:
            curr[j] -= 1
print(len(curr))
