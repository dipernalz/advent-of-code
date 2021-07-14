inpt = list(map(int, open('input.txt', 'r').read().split('\n')))

for i in range(25, len(inpt)):
	isValid = False
	for j in range(i - 25, i):
		if isValid:
			break
		for k in range(i - 25, i):
			if j != k and inpt[j] + inpt[k] == inpt[i]:
				isValid = True
				break
	if not isValid:
		print(inpt[i])
		exit()
