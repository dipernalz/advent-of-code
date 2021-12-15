# 472/530

inpt = list(map(int, open('input.txt', 'r').read().split(',')))
l, m = min(inpt), max(inpt)

# Part 1
fuel = float('inf')
for i in range(l, m + 1):
    fuel = min(fuel, sum(abs(inpt[j] - i) for j in range(len(inpt))))
print(fuel)

# Part 2
d = {0: 0}
for i in range(1, m + 1):
    d[i] = d[i - 1] + i

fuel = float('inf')
for i in range(l, m + 1):
    fuel = min(fuel, sum(d[abs(inpt[j] - i)] for j in range(len(inpt))))
print(fuel)
