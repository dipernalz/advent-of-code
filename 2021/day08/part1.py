# 158

inpt = open('input.txt', 'r').read().rstrip().split('\n')

n = 0
for i in inpt:
    i = i.split(' | ')[1]
    n += sum(1 for j in i.split() if len(j) in (2, 3, 4, 7))
print(n)
