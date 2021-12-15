import re

inpt = open('input.txt', 'r').read().split('\n\n')

validSet = set()
for i, j in re.findall(r'(\d+)-(\d+)', inpt[0]):
	validSet |= set(range(int(i), int(j) + 1))
print(sum(0 if int(i) in validSet else int(i) for i in re.findall(r'(\d+)', inpt[2])))