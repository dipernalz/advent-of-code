import heapq

path = '.'

def main():
    inpt = open('input.txt', 'r').read().strip('\n')
    maze = tuple(inpt.split('\n'))

    start, end = (-1, -1), (-1, -1)
    neighborDct, warpDct = {}, {}
    for r in range(len(maze)):
        for c in range(len(maze[r])):
            if maze[r][c] == path:
                neighborLst = []
                if maze[r - 1][c] == path: neighborLst.append((r - 1, c))
                if maze[r + 1][c] == path: neighborLst.append((r + 1, c))
                if maze[r][c - 1] == path: neighborLst.append((r, c - 1))
                if maze[r][c + 1] == path: neighborLst.append((r, c + 1))
                if (r, c) in neighborDct:
                    neighborDct[r, c] += neighborLst
                else:
                    neighborDct[r, c] = neighborLst
            elif maze[r][c].isupper():
                code = ''
                if r > 0 and r < len(maze) - 1:
                    if maze[r - 1][c].isupper() and maze[r + 1][c] == path:
                        code = maze[r - 1][c] + maze[r][c]
                        pathLoc = (r + 1, c)
                    elif maze[r + 1][c].isupper() and maze[r - 1][c] == path:
                        code = maze[r][c] + maze[r + 1][c]
                        pathLoc = (r - 1, c)
                if c > 0 and c < len(maze[r]) - 1:
                    if maze[r][c - 1].isupper() and maze[r][c + 1] == path:
                        code = maze[r][c - 1] + maze[r][c]
                        pathLoc = (r, c + 1)
                    elif maze[r][c + 1].isupper() and maze[r][c - 1] == path:
                        code = maze[r][c] + maze[r][c + 1]
                        pathLoc = (r, c - 1)
                
                if not code: continue
                if code == 'AA': start = pathLoc
                elif code == 'ZZ': end = pathLoc
                elif code in warpDct:
                    if warpDct[code] in neighborDct:
                        neighborDct[warpDct[code]] += [pathLoc]
                    else:
                        neighborDct[warpDct[code]] = [pathLoc] 
                    if pathLoc in neighborDct:
                        neighborDct[pathLoc] += [warpDct[code]]
                    else:
                        neighborDct[pathLoc] = [warpDct[code]]
                else:
                    warpDct[code] = pathLoc

    q = [(0, start)]
    distDct = {start: 0}
    while q:
        d, p = heapq.heappop(q)
        if p == end:
            print(d)
            break
        for nbr in neighborDct[p]:
            if nbr not in distDct:
                distDct[nbr] = d + 1
                q.append((d + 1, nbr))

main()

