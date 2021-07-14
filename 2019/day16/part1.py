import numpy as np

def main():
    f = open('day16.txt', 'r')
    inpt = np.array([int(i) for i in f.read().rstrip()] * 1)
    basePattern = (0, 1, 0, -1)
    
    pttrnArr = []
    for i in range(len(inpt)):
        pattern = []
        k, l = 0, 0
        for j in range(len(inpt) + 1):
            pattern.append(basePattern[k])
            l += 1
            if l > i:
                k = (k+1) % len(basePattern)
                l = 0
        pttrnArr.append(pattern[1:])
    pttrnArr = np.array(pttrnArr)
    
    for i in range(100):
        X = np.dot(pttrnArr, inpt)
        outpt = np.array([abs(j) % 10 for j in X])
        inpt = outpt

    print(''.join([str(i) for i in outpt[:8]]))

main()
