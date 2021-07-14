inpt = open('input.txt', 'r').read().split('\n')

x, y = 0, 0
wx, wy = 10, 1
directionDct = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
rightTurnDct = {90: (0, 1, -1, 0), 180: (-1, 0, 0, -1), 270: (0, -1, 1, 0)}
leftTurnDct = {90: (0, -1, 1, 0), 180: (-1, 0, 0, -1), 270: (0, 1, -1, 0)}
for i in inpt:
	instr, n = i[0], int(i[1:])
	if instr in directionDct:
		wx += directionDct[instr][0] * n
		wy += directionDct[instr][1] * n
	elif instr == 'F':
		x += wx * n
		y += wy * n
	elif instr == 'R':
		wx, wy = rightTurnDct[n][0] * wx + rightTurnDct[n][1] * wy, \
			rightTurnDct[n][2] * wx + rightTurnDct[n][3] * wy
	else:
		wx, wy = leftTurnDct[n][0] * wx + leftTurnDct[n][1] * wy, \
			leftTurnDct[n][2] * wx + leftTurnDct[n][3] * wy
print(abs(x) + abs(y))