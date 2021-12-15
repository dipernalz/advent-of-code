inpt = open('input.txt', 'r').read().split('\n')

mask, mem = '', {}
for i in inpt:
	i = i.split()
	if i[0] == 'mask':
		mask = i[2]
	else:
		addr = int(i[0].split('[')[1][:-1])
		n = str(bin(int(i[2])))[2:]
		n = '0' * (len(mask) - len(n)) + n
		mem[addr] = int(''.join(mask[j] if mask[j] != 'X' else n[j] for j in range(len(n))), 2)
print(sum(mem.values()))