def main():
    f = open('day16.txt', 'r')
    inpt = [int(i) for i in f.read().rstrip()] * 10000
    idx = int(''.join([str(i) for i in inpt[:7]])) - len(inpt) // 2
    inpt = inpt[len(inpt)//2:]
    
    for i in range(100):
        outpt = []
        n = 0
        for j in range(len(inpt) - 1, -1, -1):
            n = (n + inpt[j]) % 10
            outpt += [n]
        outpt = outpt[::-1]
        inpt = outpt
    print(''.join([str(i) for i in outpt[idx:idx+8]]))


main()
