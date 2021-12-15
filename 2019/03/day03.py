with open('day03.txt', 'r') as f:
	wires = f.readlines()
	wire1 = wires[0][:-1].split(',')
	wire2 = wires[1][:-1].split(',')
	wire1Pts = set([])
	wire2Pts = set([])
	currentPos = (0,0)
	wire1Dct = {}
	wire2Dct = {}
	steps = 1
	for d in wire1:
		for i in range(int(d[1:])):
			if d[0] == 'L':
				newPos = (currentPos[0] - 1, currentPos[1])
			elif d[0] == 'R':
				newPos = (currentPos[0] + 1, currentPos[1])
			elif d[0] == 'U':
				newPos = (currentPos[0], currentPos[1] + 1)
			elif d[0] == 'D':
				newPos = (currentPos[0], currentPos[1] - 1)
			wire1Pts.add(newPos)
			if newPos not in wire1Dct:
				wire1Dct[newPos] = steps
			currentPos = newPos
			steps += 1
	currentPos = (0,0)
	steps = 1
	for d in wire2:
		for i in range(int(d[1:])):
			if d[0] == 'L':
				newPos = (currentPos[0] - 1, currentPos[1])
			elif d[0] == 'R':
				newPos = (currentPos[0] + 1, currentPos[1])
			elif d[0] == 'U':
				newPos = (currentPos[0], currentPos[1] + 1)
			elif d[0] == 'D':
				newPos = (currentPos[0], currentPos[1] - 1)
			wire2Pts.add(newPos)
			if newPos not in wire2Dct:
				wire2Dct[newPos] = steps
			currentPos = newPos
			steps += 1
	intersections = wire1Pts & wire2Pts
	minDist = 1000000000
	for p in intersections:
		print(p)
		dist = abs(p[0]) + abs(p[1])
		if dist < minDist:
			minDist = dist
	minSteps = 1000000000
	for p in intersections:
		steps = wire1Dct[p] + wire2Dct[p]
		if steps < minSteps:
			minSteps = steps
	print(minDist)
	print(minSteps)
