import re

inpt = [s.replace(' ', '') for s in open('input.txt', 'r').read().split('\n')]

def evaluate(exp):
	nLst, opLst, i = [], [], 0
	while i < len(exp):
		if exp[i] == '(':
			n = 1
			for j in range(i + 1, len(exp)):
				if exp[j] == '(':
					n += 1
				elif exp[j] == ')':
					n -= 1
					if n == 0:
						closeParenLoc = j
						break
			nLst.append(evaluate(exp[i + 1:closeParenLoc]))
			i = closeParenLoc
		elif exp[i] in '+*':
			opLst.append(exp[i])
		else:
			nLst.append(int(exp[i]))
		i += 1
	n = nLst[0]
	for i in range(len(opLst)):
		if opLst[i] == '+':
			n += nLst[i + 1]
		else:
			n *= nLst[i + 1]
	return n

print(sum(evaluate(i) for i in inpt))