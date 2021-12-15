inpt = open('input.txt', 'r').read().split('\n')

for j in range(len(inpt)):
	inptCopy = inpt.copy()
	replacedLine = inpt[j].split()
	if replacedLine[0] == 'jmp':
		inptCopy[j] = 'nop ' + replacedLine[1]
	elif replacedLine[0] == 'nop':
		inptCopy[j] = 'jmp ' + replacedLine[1]
	else:
		continue
	acc = 0
	i = 0
	executedSet = set()
	while i < len(inptCopy):
		executedSet |= {i}
		line = inptCopy[i].split()
		if line[0] == 'jmp':
			i += int(line[1])
		elif line[0] == 'acc':
			acc += int(line[1])
			i += 1
		elif line[0] == 'nop':
			i += 1
		if i in executedSet:
			break
	if i == len(inptCopy):
		print(acc)
