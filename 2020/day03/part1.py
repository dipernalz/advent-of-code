inpt = open('input.txt', 'r').read().split('\n')
print(sum(1 if inpt[i][(i * 3) % len(inpt[i])] == '#' else 0 for i in range(len(inpt))))