f = open('day05.txt', 'r')
intcode = [int(l.rstrip('\n')) for l in f.read().split(',')]
inpt = 5
i = 0
while True:
	intcodeStr = '0' * (5 - len(str(intcode[i]))) + str(intcode[i])
	opcode = intcodeStr[3:]

	if opcode == '99':
		# print(intcode)
		break

	mode1 = intcodeStr[2]
	if mode1 == '0': p1 = intcode[i + 1]
	else: p1 = i + 1

	if opcode == '03':
		intcode[p1] = inpt
		i += 2
		continue
	if opcode == '04':
		print(intcode[p1])
		i += 2
		continue

	mode2 = intcodeStr[1]
	if mode2 == '0': p2 = intcode[i + 2]
	else: p2 = i + 2

	if opcode == '05':
		if intcode[p1] != 0: i = intcode[p2]
		else: i += 3
		continue
	if opcode == '06':
		if intcode[p1] == 0: i = intcode[p2]
		else: i += 3
		continue

	mode3 = intcodeStr[0]
	if mode3 == '0': p3 = intcode[i + 3]
	else: p3 = i + 3

	if opcode == '01':
		intcode[p3] = intcode[p1] + intcode[p2]
		i += 4
		continue
	if opcode == '02':
		intcode[p3] = intcode[p1] * intcode[p2]
		i += 4
		continue
	if opcode == '07':
		if intcode[p1] < intcode[p2]: intcode[p3] = 1
		else: intcode[p3] = 0
		i += 4
		continue
	if opcode == '08':
		if intcode[p1] == intcode[p2]: intcode[p3] = 1
		else: intcode[p3] = 0
		i += 4
		continue
