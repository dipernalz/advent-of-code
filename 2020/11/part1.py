inpt = open('input.txt', 'r').read().split('\n')

adjSeatDct = {}
nRows = len(inpt)
nCols = len(inpt[0])
for i in range(nRows):
	for j in range(nCols):
		if inpt[i][j] == '.':
			pass
		adjLst = []
		for dr in range(-1, 2):
			for dc in range(-1, 2):
				if (dr != 0 or dc != 0) and 0 <= i + dr < nRows and 0 <= j + dc < nCols:
					adjLst.append((i + dr, j + dc))
		adjSeatDct[(i, j)] = adjLst

changed = False
while not changed:
	inptCopy = inpt.copy()
	for i in range(nRows):
		for j in range(nCols):
			nList = [inptCopy[r][c] for r, c in adjSeatDct[(i, j)]]
			if inptCopy[i][j] == 'L' and '#' not in nList:
				inpt[i] = inpt[i][:j] + '#' + inpt[i][j + 1:]
			if inptCopy[i][j] == '#' and nList.count('#') >= 4:
				inpt[i] = inpt[i][:j] + 'L' + inpt[i][j + 1:]
	if inptCopy == inpt:
		changed = True
print(''.join(inpt).count('#'))
