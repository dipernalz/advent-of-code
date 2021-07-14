import re

inpt = open('input.txt', 'r').read().split('\n\n')

rulesLst = inpt[0].split('\n')
n = len(rulesLst)
validLst, validSet = [set() for i in range(n)], set()
for i in range(n):
	for j, k in re.findall(r'(\d+)-(\d+)', rulesLst[i]):
		validLst[i] |= set(range(int(j), int(k) + 1))
		validSet |= set(range(int(j), int(k) + 1))

nearbyLst, possibleSetLst = inpt[2].split('\n')[1:], [set(range(n)) for i in range(n)]
for i in range(len(nearbyLst)):
	isValid = True
	for j in re.findall(r'(\d+)', nearbyLst[i]):
		if int(j) not in validSet:
			isValid = False
			break
	if not isValid:
		continue
	c = 0
	for j in re.findall(r'(\d+)', nearbyLst[i]):
		for k in range(n):
			if int(j) not in validLst[k]:
				possibleSetLst[c] -= {k}
		c += 1

indexDct = {}
for i in range(n):
	for j in range(n):
		if len(possibleSetLst[j]) == 1:		
			idx = possibleSetLst[j].pop()
			indexDct[idx] = j
			for k in range(len(possibleSetLst)):
				possibleSetLst[k] -= {idx}
			break
myTicket, total = inpt[1].split('\n')[1].split(','), 1
for i in range(6):
	total *= int(myTicket[indexDct[i]])
print(total)