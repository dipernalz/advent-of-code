# 81/138

inpt = list(map(int, open('input.txt', 'r').read().split('\n')))

# Part 1
n = 0
for i in range(1, len(inpt)):
    if inpt[i] > inpt[i - 1]:
        n += 1
print(n)

# Part 2
n = 0
for i in range(1, len(inpt) - 2):
    if (inpt[i] + inpt[i + 1] + inpt[i + 2] >
            inpt[i] + inpt[i + 1] + inpt[i - 1]):
        n += 1
print(n)
