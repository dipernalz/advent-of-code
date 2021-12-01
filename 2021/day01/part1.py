# 81

inpt = list(map(int, open('input.txt', 'r').read().split('\n')))

n = 0
for i in range(1, len(inpt)):
    if inpt[i] > inpt[i-1]:
        n += 1
print(n)
