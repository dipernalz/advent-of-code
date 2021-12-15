with open('day02.txt', 'r') as f:
	ogIntcode = [int(l.rstrip('\n')) for l in f.read().split(',')]
	for noun in range(100):
		for verb in range(100):
			intcode = ogIntcode.copy()
			intcode[1] = noun
			intcode[2] = verb
			i = 0
			while True:
				if (intcode[i] == 99):
					if intcode[0] == 19690720:
						print(100 * noun + verb)
					break
				elif intcode[i] == 1:
					intcode[intcode[i+3]] = intcode[intcode[i+1]] + intcode[intcode[i+2]]
				elif intcode[i] == 2:
					intcode[intcode[i+3]] = intcode[intcode[i+1]] * intcode[intcode[i+2]]
				i += 4
