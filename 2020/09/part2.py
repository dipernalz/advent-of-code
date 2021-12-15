inpt = list(map(int, open('input.txt', 'r').read().split('\n')))
n = 14360655

start, end = 0, 1
total = inpt[start]
while total != n:
	if total > n:
		total -= inpt[start]
		start += 1
	else:
		total += inpt[end]
		end += 1

contigLst = [inpt[i] for i in range(start, end)]
print(min(contigLst) + max(contigLst))
