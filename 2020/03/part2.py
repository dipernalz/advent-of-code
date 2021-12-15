inpt = open('input.txt', 'r').read().split('\n')
treeLst = [sum(1 if inpt[i * d][(i * r) % len(inpt[i])] == '#' else 0 for i in range(len(inpt) // d)) for r, d in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))]
print(treeLst[0] * treeLst[1] * treeLst[2] * treeLst[3] * treeLst[4])