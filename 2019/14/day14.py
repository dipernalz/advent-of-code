import math

reactionDct = {}
chemDct = {}
extraDct = {}

def main():
    inpt = [l.rstrip().split(' => ') for l in open('day14.txt', 'r').readlines()]
    for i in inpt:
        inptChems = i[0].split(', ')
        outptChem = i[1]
        j = [c.split() for c in inptChems]
        k = outptChem.split()
        reactionDct[(int(k[0]), k[1])] = tuple([(int(c[0]), c[1]) for c in j])
        chemDct[k[1]] = (int(k[0]), k[1])
        extraDct[k[1]] = 0
    #print(oreRequired((1, 'FUEL')))
    print(potentialFuel(10 ** 12))

def oreRequired(chemicalData):
    chemical = chemicalData[1]
    nRequired = chemicalData[0]
    nPerReaction = chemDct[chemical][0]
    nExtra = extraDct[chemical]
    if nExtra >= nRequired:
        extraDct[chemical] = nExtra - nRequired
        return 0
    nReactions = math.ceil((nRequired - nExtra) / nPerReaction)
    extraDct[chemical] = (nReactions * nPerReaction) - (nRequired - nExtra)
    nOre = 0
    for inpt in reactionDct[(nPerReaction, chemical)]:
        if inpt[1] == 'ORE':
            return nReactions * inpt[0]
        nOre += oreRequired((nReactions * inpt[0], inpt[1]))
    return nOre

def potentialFuel(nOre):
    nFuel = 0
    while nOre > 0:
        nOre -= oreRequired((1, 'FUEL'))
        nFuel += 1
    return nFuel - (1 if nOre < 0 else 0)

main()
