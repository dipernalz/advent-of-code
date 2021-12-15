def main():
    intcode = [int(l.rstrip('\n')) for l in open('part1.txt', 'r').read().split(',')]
    runIntcode(intcode)

def runIntcode(intcode, inptLst=[], i=0, inptIdx=0, relativeBase=0):
    view = ''
    while True:
        intcodeStr = '0' * (5 - len(str(intcode[i]))) + str(intcode[i])
        opcode = intcodeStr[3:]

        if opcode == '99': # program is finished
            x = view.rstrip().split('\n')
            n = 0
            for i in range(1, len(x) - 1):
                for j in range(1, len(x[0]) - 1):
                    if x[i][j] != '#': continue
                    if x[i-1][j] != '#' or x[i+1][j] != '#' \
                    or x[i][j-1] != '#' or x[i][j+1] != '#': continue
                    n += i * j
            print(n)
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
            #print(intcode[p1])
            view += chr(intcode[p1])
            i += 2
            continue
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
