def main():
	intcode = [int(l.rstrip('\n')) for l in open('day07.txt', 'r').read().split(',')]

	psblInpts = []
	for i in range(5, 10):
		for j in range(5, 10):
			for k in range(5, 10):
				for l in range(5, 10):
					for m in range(5, 10):
						if len(set((i, j, k, l, m))) == 5:
							psblInpts.append((i, j, k, l, m))

	maxSignal = 0
	for inpt in psblInpts:
		intcodeStateLst = [[intcode.copy(), [inpt[i], 0] if i == 0 else [inpt[i]], 0, 0] for i in range(5)]
		while True:
			for i in range(5):
				result = runIntcode(intcodeStateLst[i][0], intcodeStateLst[i][1], intcodeStateLst[i][2], intcodeStateLst[i][3])
				if not result[0]:
					if i != 4:
						intcodeStateLst[i + 1][1].append(result[1])
					else:
						intcodeStateLst[0][1].append(result[1])
						output = result[1]
				intcodeStateLst[i][2] = result[2]
				intcodeStateLst[i][3] = result[3]
			if result[0]:
				break
		if output > maxSignal:
			maxSignal = output
	print(maxSignal)


def runIntcode(intcode, inptLst, i, inptIdx):
	while True:
		intcodeStr = '0' * (5 - len(str(intcode[i]))) + str(intcode[i])
		opcode = intcodeStr[3:]

		if opcode == '99':
			return True, 0, 0, 0

		mode1 = intcodeStr[2]
		if mode1 == '0': p1 = intcode[i + 1]
		else: p1 = i + 1

		if opcode == '03':
			intcode[p1] = inptLst[inptIdx]
			inptIdx += 1
			i += 2
			continue
		if opcode == '04':
			return False, intcode[p1], i + 2, inptIdx

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


main()
