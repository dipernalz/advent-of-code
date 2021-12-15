fieldSet = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
n = 0
for passport in open('input.txt', 'r').read().split('\n\n'):
	passportFieldSet = set([])
	for data in passport.split():
		data = data.split(':')
		if data[0] in fieldSet:
			if data[0] == 'byr' and 1920 <= int(data[1]) <= 2002:
				passportFieldSet.add(data[0])
			elif data[0] == 'iyr' and 2010 <= int(data[1]) <= 2020:
				passportFieldSet.add(data[0])
			elif data[0] == 'eyr' and 2020 <= int(data[1]) <= 2030:
				passportFieldSet.add(data[0])
			elif data[0] == 'hgt' and \
				(data[1][-2:] == 'in' and 59 <= int(data[1][:-2]) <= 76 or \
				data[1][-2:] == 'cm' and 150 <= int(data[1][:-2]) <= 193):
				passportFieldSet.add(data[0])
			elif data[0] == 'hcl' and data[1][0] == '#' and \
				False not in {True if y in '0123456789abcdef' else False for y in data[1][1:]}:
				passportFieldSet.add(data[0])
			elif data[0] == 'ecl' and data[1] in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
				passportFieldSet.add(data[0])
			elif len(data[1]) == 9 and \
				False not in {True if y in '0123456789' else False for y in data[1]}:
				passportFieldSet.add(data[0])

	if fieldSet.issubset(passportFieldSet):
		n += 1

print(n)