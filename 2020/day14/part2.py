inpt = open('input.txt', 'r').read().split('\n')

mask, mem = '', {}
for i in inpt:
	i = i.split()
	if i[0] == 'mask':
		mask = i[2]
	else:
		addr = str(bin(int(i[0].split('[')[1][:-1])))[2:]
		addr = '0' * (len(mask) - len(addr)) + addr
		q = [''.join('1' if mask[j] == '1' else addr[j] if mask[j] == '0' else 'X' \
			for j in range(len(mask)))]
		while q:
			a = q.pop()
			if 'X' in a:
				xIdx = a.index('X')
				q.append(a[:xIdx] + '0' + a[xIdx + 1:])
				q.append(a[:xIdx] + '1' + a[xIdx + 1:])
			else:
				mem[int(a, 2)] = int(i[2])
print(sum(mem.values()))