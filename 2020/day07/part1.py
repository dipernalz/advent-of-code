inpt = open('input.txt', 'r').read().split('\n')

containedInDct = {}
for rule in inpt:
	rule = rule.split(' contain ')
	container = rule[0].split(' ')[0] + ' ' + rule[0].split(' ')[1]
	for r in rule[1].split(', '):
		if r != 'no other bags.':
			r = r.split()
			bag = r[1] + ' ' + r[2]
			if bag in containedInDct:
				containedInDct[bag].append(container)
			else:
				containedInDct[bag] = [container]

containsSet = set()
queue = ['shiny gold']
while queue:
	bag = queue.pop()
	if bag not in containedInDct:
		continue
	for b in containedInDct[bag]:
		containsSet.add(b)
		queue.append(b)
print(len(containsSet))