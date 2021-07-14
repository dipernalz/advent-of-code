inpt = open('input.txt', 'r').read().split('\n')

containsDct = {}
for rule in inpt:
	rule = rule.split(' contain ')
	container = rule[0].split(' ')[0] + ' ' + rule[0].split(' ')[1]
	containsList = []
	for r in rule[1].split(', '):
		if r != 'no other bags.':
			r = r.split()
			bag = r[1] + ' ' + r[2]
			containsList.append((int(r[0]), r[1] + ' ' + r[2]))
	containsDct[container] = containsList

def nBagsIn(bag):
	if bag not in containsDct:
		return 0
	return sum(i[0] for i in containsDct[bag]) + sum(i[0] * nBagsIn(i[1]) for i in containsDct[bag])
print(nBagsIn('shiny gold'))