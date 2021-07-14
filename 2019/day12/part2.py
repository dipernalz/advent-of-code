import re

def main():
    regex = re.compile(r'-?\d+')
    pLst, vLst = [], [(0, 0, 0) for i in range(4)]
    with open('day12.txt', 'r') as f:
        for moon in f:
            pLst.append(tuple(int(i) for i in regex.findall(moon)))

    for i in range(1000):
        dtLst = []
        for j in range(4):
            dt = []
            for k in range(3):
                d = 0
                for l in range(4):
                    if j != l:
                        if pLst[j][k] < pLst[l][k]:
                            d += 1
                        elif pLst[j][k] > pLst[l][k]:
                            d -= 1
                dt.append(d)
            dtLst.append(tuple(dt))
        for j in range(4):
            vLst[j] = (vLst[j][0] + dtLst[j][0], vLst[j][1] + dtLst[j][1], 
                       vLst[j][2] + dtLst[j][2])
            pLst[j] = (pLst[j][0] + vLst[j][0], pLst[j][1] + vLst[j][1], 
                       pLst[j][2] + vLst[j][2])

    print(energy(pLst, vLst))


def energy(pLst, vLst):
    e = 0
    for i in range(4):
        pe = sum(abs(pLst[i][j]) for j in range(3))
        ke = sum(abs(vLst[i][j]) for j in range(3))
        e += pe * ke
    return e 


main()
