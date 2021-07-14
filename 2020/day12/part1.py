inpt = open('input.txt', 'r').read().split('\n')

x, y, direction = 0, 0, 'E'
directionLst = ['N', 'E', 'S', 'W']
directionDct = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
for i in inpt:
	instr, n = i[0], int(i[1:])
	if instr == 'F':
		x += directionDct[direction][0] * n
		y += directionDct[direction][1] * n
	elif instr in directionDct:
		x += directionDct[instr][0] * n
		y += directionDct[instr][1] * n
	else:
		direction = directionLst[int((directionLst.index(direction) + \
			(n if instr == 'R' else -n) / 90) % 4)]
print(abs(x) + abs(y))