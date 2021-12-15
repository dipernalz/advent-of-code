inpt = open('input.txt', 'r').read().split('\n')

n, stop, dt = int(inpt[0]), 0, 10 ** 10
for i in inpt[1].split(','):
	if i != 'x':
		i = int(i)
		if i - n % i < dt:
			stop, dt = i, i - n % i
print(dt * stop)