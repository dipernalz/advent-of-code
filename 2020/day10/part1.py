inpt = list(map(int, open('input.txt', 'r').read().split('\n')))
inpt.append(0)
inpt.sort()

total1 = 0
total3 = 1
for i in range(len(inpt)):
	if inpt[i] - inpt[i - 1] == 1:
		total1 += 1
	elif inpt[i] - inpt[i - 1] == 3:
		total3 += 1
print(total1 * total3)
