def main():
	image = open('day08.txt', 'r').read().rstrip('\n')
	width = 25
	height = 6
	layerLst = [image[i:i+width*height] for i in range(0, len(image), width * height)]
	idx = -1
	minZeros = width * height
	for i in range(len(layerLst)):
		c = layerLst[i].count('0')
		if c < minZeros:
			idx = i
			minZeros = c
	print(layerLst[idx].count('1') * layerLst[idx].count('2'))

	outputLst = [d for d in layerLst[0]]
	for i in range(1, len(layerLst)):
		for j in range(len(layerLst[i])):
			if outputLst[j] == '2':
				outputLst[j] = layerLst[i][j]

	for i in range(height):
		for j in range(width):
			print('# ' if outputLst[i*width+j] == '1' else '  ', end='')
		print()


main()
