inpt = [int(s) for s in open('input.txt', 'r').read().split('\n')]

for i in range(len(inpt)):
	for j in range(1, len(inpt)):
		if 2020 - inpt[i] - inpt[j] in inpt:
			print(inpt[i] * inpt[j] * (2020 - inpt[i] - inpt[j]))
			exit()