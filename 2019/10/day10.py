import math

def main():
    asteroid = '#'
    
    asteroidLst = []
    r = 0
    with open('day10.txt', 'r') as map:
        for row in map:
            row = row.rstrip()
            # print(row)
            c = 0
            for col in row:
                if col == '#':
                    asteroidLst.append((c, r))
                c += 1
            r += 1
    
    asteroidDetectDct = {}
    for asteroid in asteroidLst:
        asteroidDetectDct[asteroid] = 0
        slopeSet = set([])
        for a in asteroidLst:
            if a != asteroid:
                slope = calcSlope(asteroid, a)
                if slope not in slopeSet:
                    slopeSet.add(slope)
                    asteroidDetectDct[asteroid] += 1
    
    maxAsteroid, asteroid = -1, (-1, -1)
    for a in asteroidDetectDct:
        if asteroidDetectDct[a] > maxAsteroid:
            maxAsteroid, asteroid = asteroidDetectDct[a], a
    print(asteroid, maxAsteroid)

    angleDct = {}
    for a in asteroidLst:
        if a != asteroid:
            angle = calcAngle(asteroid, a)
            if angle not in angleDct:
                angleDct[angle] = [a]
            else:
                angleDct[angle].append(a)
    for angle in angleDct:
        angleDct[angle].sort(key=lambda a: distance(a, asteroid))
    angleLst = sorted(angleDct)
    angle = min(angleLst)
    p = 0
    for i in range(200):
        a = angleDct[angleLst[p]].pop()
        if len(angleDct[angleLst[p]]) == 0:
            del angleDct[angleLst[p]]
        p += 1
    print(a[0] * 100 + a[1])


def calcSlope(a1, a2):
    if (a2[0] - a1[0] == 0):
        if a2[1] > a1[1]:
            return (1000, False)
        else:
            return (1000, True)
    return ((a2[1] - a1[1]) / (a2[0] - a1[0]), a1[0] > a2[0])

def calcAngle(a1, a2):
    x, y = a2[0] - a1[0], a1[1] - a2[1]
    if x > 0:
        if y > 0:
            return math.atan(x / y)
        elif y == 0:
            return math.pi / 2
        else:
            return math.pi + math.atan(x / y)
    elif x == 0:
        if y > 0:
            return 0
        else:
            return math.pi
    else:
        if y < 0:
            return math.pi + math.atan(x / y)
        elif y == 0:
            return math.pi * 3 / 2
        else:
            return 2 * math.pi + math.atan(x / y)

def distance(a1, a2):
    return -1 * (a2[0] - a1[0]) ** 2 + (a2[1] - a1[1]) ** 2

main()
