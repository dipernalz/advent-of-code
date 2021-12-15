inpt = open('input.txt', 'r').read().split('\n')

cubeDct = {}
for i in range(len(inpt)):
	for j in range(len(inpt[0])):
		cubeDct[i, j, 0, 0] = inpt[i][j]
for i in range(6):
	cubeDctCopy = cubeDct.copy()
	for cube in cubeDct:
		for j in range(-1, 2):
			for k in range(-1, 2):
				for l in range(-1, 2):
					for m in range(-1, 2):
						if not (j == 0 and k == 0 and l == 0 and m == 0):
							nbr = (cube[0] + j, cube[1] + k, cube[2] + l, cube[3] + m)
							if nbr not in cubeDct:
								cubeDctCopy[nbr] = '.'
	for cube in cubeDctCopy:
		n = 0
		for j in range(-1, 2):
			for k in range(-1, 2):
				for l in range(-1, 2):
					for m in range(-1, 2):
						if not (j == 0 and k == 0 and l == 0 and m == 0):
							nbr = (cube[0] + j, cube[1] + k, cube[2] + l, cube[3] + m)
							if nbr in cubeDctCopy and cubeDctCopy[nbr] == '#':
								n += 1
		if cubeDctCopy[cube] == '#' and n not in (2, 3):
			cubeDct[cube] = '.'
		elif n == 3:
			cubeDct[cube] = '#'
print(list(cubeDct.values()).count('#'))