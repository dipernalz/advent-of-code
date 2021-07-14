inpt = open('input.txt', 'r').read().split('\n')[1].split(',')

n, incr = 0, -1
for i in range(len(inpt)):
	if inpt[i] != 'x':
		if incr == -1:
			incr = int(inpt[i])
			continue
		while (n + i) % int(inpt[i]) != 0:
			n += incr
		incr *= int(inpt[i])
print(n)