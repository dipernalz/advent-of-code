with open('day01.txt', 'r') as f:
	modules = [int(l.rstrip('\n')) for l in f.readlines()]
	print(sum([int(n/3) - 2 for n in modules]))

	# part 2
	i = 0
	s = 0
	while i != len(modules):
		n = int(modules[i]/3) - 2
		if (n > 0):
			s += n
			modules.append(n)
		i += 1
	print(s)
