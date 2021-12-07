# 472

inpt = list(map(int, open('input.txt', 'r').read().split(',')))
l, m = min(inpt), max(inpt)

fuel = float('inf')
for i in range(l, m + 1):
    fuel = min(fuel, sum(abs(inpt[j] - i) for j in range(len(inpt))))
print(fuel)
