inpt = list(map(int, open('input.txt', 'r').read().split(',')))

n, numDct = 0, {}
for i in range(len(inpt)):
	numDct[inpt[i]] = [i]
	n = inpt[i]
for i in range(len(numDct), 2020):
	if n in numDct and len(numDct[n]) == 2:
		n = numDct[n][1] - numDct[n][0]
		if n in numDct:
			numDct[n] = [numDct[n][-1], i]
		else:
			numDct[n] = [i]
	else:
		numDct[0] = [numDct[0][-1], i]
		n = 0
print(n)