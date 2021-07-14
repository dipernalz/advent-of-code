inpt = open('input.txt', 'r').read().split('\n')

acc = 0
i = 0
executedSet = set()
while i < len(inpt):
	executedSet |= {i}
	line = inpt[i].split()
	if line[0] == 'jmp':
		i += int(line[1])
	elif line[0] == 'acc':
		acc += int(line[1])
		i += 1
	elif line[0] == 'nop':
		i += 1
	if i in executedSet:
		print(acc)
		break
