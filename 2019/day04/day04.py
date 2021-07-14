import re

x = 0
for j in range(197487, 673251 + 1):
	s = str(j)

	b = True
	for i in range(5):
		if int(s[i+1]) < int(s[i]):
			b = False
			break
	if not b:
		continue

	b = False
	for i in range(5):
		if s[i] == s[i+1]:
			if i == 4 or s[i] != s[i+2]:
				if i == 0 or s[i] != s[i-1]:
					b = True
					break
	if not b:
		continue

	x += 1
print(x)
