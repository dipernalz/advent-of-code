"""
ABCDE

 1002

DE - two-digit opcode,      02 == opcode 2

 C - mode of 1st parameter,  0 == position mode

 B - mode of 2nd parameter,  1 == immediate mode

 A - mode of 3rd parameter,  0 == position mode,
                                  omitted due to being a leading zero

 - In position mode (0), a parameter is interpreted as a position
 - In immediate mode (1), a parameter is interpreted as a value
 - In relative mode (2), a parameter is interpreted as a position, but count from the relative base rather than 0
"""

def main():
    intcode = [int(l.rstrip('\n')) for l in open('day11.txt', 'r').read().split(',')]
    runIntcode(intcode, inptLst=[1])

def runIntcode(intcode, inptLst=[], i=0, inptIdx=0, relativeBase=0):
    direction = 'u'
    currentPos = (0, 0)
    colorDct = {}
    outputLst = []
    directionDct = {'u': (0, 1), 'l': (-1, 0), 'r': (1, 0), 'd': (0, -1)}
    turnDct = {('u', 0): 'l', ('l', 0): 'd', ('d', 0): 'r', ('r', 0): 'u',
               ('u', 1): 'r', ('r', 1): 'd', ('d', 1): 'l', ('l', 1): 'u'}
    while True:
        intcodeStr = '0' * (5 - len(str(intcode[i]))) + str(intcode[i])
        opcode = intcodeStr[3:]

        if opcode == '99': # program is finished
            print(len(colorDct))
            coordLst = sorted(colorDct, key=lambda x: -x[1]*100+x[0])
            xMax = max(x[0] for x in coordLst)
            yMin = min(x[1] for x in coordLst)
            printDct = {0: '.', 1: '#'}
            for j in range(0, yMin - 1, -1):
                for k in range(xMax + 1):
                    if (k, j) in colorDct:
                        print(printDct[colorDct[(k, j)]], end=' ')
                    else:
                        print('.', end=' ')
                print()
            return

        mode1 = intcodeStr[2] # mode of parameter 1
        if mode1 == '0': p1 = intcode[i + 1]
        elif mode1 == '1': p1 = i + 1
        else: p1 = relativeBase + intcode[i + 1]
        if len(intcode) <= p1: intcode += (p1 - len(intcode) + 1) * [0]

        if opcode == '03': # takes an input value and stores it at address of parameter
            intcode[p1] = inptLst[inptIdx]
            inptIdx += 1
            i += 2
            continue
        if opcode == '04': # outputs the value of its parameter
            # print(intcode[p1])
            outputLst.append(intcode[p1])
            if len(outputLst) == 2:
                colorDct[currentPos] = outputLst[0]
                direction = turnDct[direction, outputLst[1]]
                currentPos = (currentPos[0] + directionDct[direction][0],
                              currentPos[1] + directionDct[direction][1])
                if currentPos in colorDct:
                    inptLst.append(colorDct[currentPos])
                else:
                    inptLst.append(0)
                outputLst = []
            i += 2
            continue
        if opcode == '09': # adjusts the relative base by the value of its only parameter
            relativeBase += intcode[p1]
            # relativeBase += p1 RIP LOL
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
