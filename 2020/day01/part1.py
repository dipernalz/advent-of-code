inpt = [int(s) for s in open('input.txt', 'r').read().split('\n')]

for i in range(len(inpt)):
	if 2020 - inpt[i] in inpt:
		print(inpt[i] * (2020 - inpt[i]))
		exit()