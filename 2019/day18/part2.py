import heapq


wall, loc = '#', '@'


def main():
    inpt = open('part2.txt', 'r').read()
    maze = tuple(inpt.split())
    
    positionLst = []
    keyDct, doorDct, doorPosDct, neighborDct = {}, {}, {}, {}
    for r in range(len(maze)):
        for c in range(len(maze[r])):
            if maze[r][c] == loc:
                positionLst.append((r, c))
            if maze[r][c].islower():
                keyDct[(r, c)] = maze[r][c]
            elif maze[r][c].isupper():
                doorDct[(r, c)] = maze[r][c]
                doorPosDct[maze[r][c]] = (r, c)
            if maze[r][c] != wall:
                neighborLst = []
                if maze[r - 1][c] != wall: neighborLst.append((r - 1, c))
                if maze[r + 1][c] != wall: neighborLst.append((r + 1, c))
                if maze[r][c - 1] != wall: neighborLst.append((r, c - 1))
                if maze[r][c + 1] != wall: neighborLst.append((r, c + 1))
                neighborDct[(r, c)] = tuple(neighborLst)
    positionLst = tuple(positionLst)

    queue = [(len(keyDct), 0, positionLst, set(keyDct), set(doorDct))]
    seenDct = {}
    minDist = 10 ** 9
    while queue:
        l, dist, posLst, keySet, doorSet = heapq.heappop(queue)

        if dist >= minDist:
            continue
        if not keySet:
            minDist = dist
            continue

        x = (tuple(keySet), posLst) 
        if x in seenDct and dist >= seenDct[x]: continue
        else: seenDct[x] = dist
        
        for i in range(4):
            pos = posLst[i]
            q = [(0, pos)]
            distDct = {pos: 0}
            while q:
                d, p = heapq.heappop(q)
                if p in doorSet: continue
                if p in keySet:
                    newDoorSet = doorSet.copy()
                    if keyDct[p].capitalize() in doorPosDct:
                        newDoorSet.remove(doorPosDct[keyDct[p].capitalize()])
                    newPosLst = tuple([posLst[j] if j != i else p for j in range(4)]) 
                    heapq.heappush(
                        queue, (l - 1, dist + d, newPosLst, keySet - {p}, newDoorSet))
                    continue
                for nbr in neighborDct[p]:
                    if nbr not in distDct:
                        distDct[nbr] = d + 1
                        q.append((d + 1, nbr))

    print(minDist)

main()

