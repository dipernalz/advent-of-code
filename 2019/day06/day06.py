with open('day06.txt', 'r') as f:
	orbits = [l.rstrip('\n') for l in f.readlines()]
	
	orbitDct = {}
	connectedOrbitDct = {}
	for obj in orbits:
		l = obj.split(')')
		if l[0] not in orbitDct:
			orbitDct[l[0]] = [l[1]]
		else:
			orbitDct[l[0]].append(l[1])

		if l[0] not in connectedOrbitDct:
			connectedOrbitDct[l[0]] = [l[1]]
		else:
			connectedOrbitDct[l[0]].append(l[1])
		if l[1] not in connectedOrbitDct:
			connectedOrbitDct[l[1]] = [l[0]]
		else:
			connectedOrbitDct[l[1]].append(l[0])

	numOrbitsDct = {'COM': 0}
	queue = ['COM']
	i = 0
	s = 0
	while i < len(queue):
		obj = queue[i]
		s += numOrbitsDct[obj]
		if obj in orbitDct:
			for o in orbitDct[obj]:
				numOrbitsDct[o] = numOrbitsDct[obj] + 1
			queue += orbitDct[obj]
		i += 1
	print(s)

	openSet = ['YOU']
	seenSet = {'YOU': 0}
	i = 0
	while i < len(queue):
		obj = openSet[i]
		d = seenSet[obj]
		if obj == 'SAN':
			print(d - 2)
			break
		for o in connectedOrbitDct[obj]:
			if o not in seenSet:
				openSet.append(o)
				seenSet[o] = d + 1
		i += 1
