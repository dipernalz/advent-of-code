directionDct = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}


def main():
    intcode = [int(l.rstrip('\n')) for l in open('day15.txt', 'r').read().split(',')]
    queue = [(1, (intcode.copy(), [], 0), (0, 0))]
    seenSet = set([])
    while len(queue) > 0:
        x = queue.pop(0)
        if x[2] in seenSet:
            continue
        seenSet.add(x[2])
        if x[0] == 2:
            print(len(x[1][1]))
            systemData = x
            break
        if x[0] == 1:
            for j in range(1, 5):
                inpt = x[1]
                outpt = runIntcode(inpt[0].copy(), inptLst=inpt[1].copy() + [j], 
                                   i=inpt[2])
                queue.append((outpt[0], outpt[1], (x[2][0] + directionDct[j][0],
                                                   x[2][1] + directionDct[j][1])))
    
    queue = [(1, (systemData[1][0], [], systemData[1][2]), systemData[2])]
    seenSet = set([])
    maxDepth = -1
    while len(queue) > 0:
        x = queue.pop(0)
        if x[2] in seenSet:
            continue
        seenSet.add(x[2])
        if x[0] == 0:
            if len(x[1][1]) + 1 > maxDepth:
                maxDepth = len(x[1][1]) + 1
            continue
        if x[0] == 1:
            for j in range(1, 5):
                inpt = x[1]
                outpt = runIntcode(inpt[0].copy(), inptLst=inpt[1].copy() + [j],
                                   i=inpt[2])
                queue.append((outpt[0], outpt[1], (x[2][0] + directionDct[j][0],
                                                   x[2][1] + directionDct[j][1])))
    print(maxDepth)


def runIntcode(intcode, inptLst=[], i=0, relativeBase=0):
    while True:
        intcodeStr = '0' * (5 - len(str(intcode[i]))) + str(intcode[i])
        opcode = intcodeStr[3:]
        if opcode == '99': # program is finished
            return

        mode1 = intcodeStr[2] # mode of parameter 1
        if mode1 == '0': p1 = intcode[i + 1]
        elif mode1 == '1': p1 = i + 1
        else: p1 = relativeBase + intcode[i + 1]
        if len(intcode) <= p1: intcode += (p1 - len(intcode) + 1) * [0]

        if opcode == '03': # takes an input value and stores it at address of parameter
            intcode[p1] = inptLst[-1]
            i += 2
            continue
        if opcode == '04': # outputs the value of its parameter
            i += 2
            return intcode[p1], (intcode.copy(), inptLst.copy(), i)
        if opcode == '09': # adjusts the relative base by the value of its only parameter
            relativeBase += intcode[p1]
            i += 2
            continue

        mode2 = intcodeStr[1] # mode of parameter 2
        if mode2 == '0': p2 = intcode[i + 2]
        elif mode2 == '1': p2 = i + 2
        else: p2 = relativeBase + intcode[i + 2]
        if len(intcode) <= p2: intcode += (p2 - len(intcode) + 1) * [0]

        if opcode == '05': # jump-if-true - if the first parameter is non-zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
            if intcode[p1] != 0: i = intcode[p2]
            else: i += 3
            continue
        if opcode == '06': # jump-if-false - if the first parameter is zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
            if intcode[p1] == 0: i = intcode[p2]
            else: i += 3
            continue

        mode3 = intcodeStr[0] # mode of parameter 3
        if mode3 == '0': p3 = intcode[i + 3]
        elif mode3 == '1': p3 = i + 3
        else: p3 = relativeBase + intcode[i + 3]
        if len(intcode) <= p3: intcode += (p3 - len(intcode) + 1) * [0]

        if opcode == '01': # adds together numbers read from two positions and stores the result in a third position
            intcode[p3] = intcode[p1] + intcode[p2]
            i += 4
            continue
        if opcode == '02': # like 01, except it multiplies instead of adding
            intcode[p3] = intcode[p1] * intcode[p2]
            i += 4
            continue
        if opcode == '07': # less than: if the first parameter is less than the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
            if intcode[p1] < intcode[p2]: intcode[p3] = 1
            else: intcode[p3] = 0
            i += 4
            continue
        if opcode == '08': # equals: if the first parameter is equal to the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
            if intcode[p1] == intcode[p2]: intcode[p3] = 1
            else: intcode[p3] = 0
            i += 4
            continue


main()
