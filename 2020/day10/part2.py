inpt = list(map(int, open('input.txt', 'r').read().split('\n')))
inpt.append(0)
inpt.sort()

def nPaths(inpt, start, end):
	n = 0
	if start >= end:
		return 0
	if start == end - 1:
		return 1
	for i in range(1, 4):
		if inpt[start] + i in inpt[start + 1:start + 4]:
			n += nPaths(inpt, start + 1 + inpt[start + 1:start + 4].index(inpt[start] + i), end)
	return n

nPathsForward = []
for i in range(len(inpt) - 1):
	nPathsForward.append(sum(1 if inpt[i] + j in inpt else 0 for j in range(1, 4)))

n, i = 1, 0
while i < len(nPathsForward):
	if nPathsForward[i] == 1:
		i += 1
		continue
	else:
		startIdx = i
		while i < len(nPathsForward) and nPathsForward[i] != 1:
			i += 1
		i += 2
		n *= nPaths(inpt, startIdx, i)
print(n)
