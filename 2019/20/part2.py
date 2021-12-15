import heapq

path = '.'

def main():
    inpt = open('input.txt', 'r').read().strip('\n')
    maze = tuple(inpt.split('\n'))

    start, end = (-1, -1), (-1, -1)
    neighborDct, warpDct, recurseDct = {}, {}, {}
    for r in range(len(maze)):
        for c in range(len(maze[r])):
            if maze[r][c] == path:
                neighborLst = []
                if maze[r - 1][c] == path: neighborLst.append((r - 1, c))
                if maze[r + 1][c] == path: neighborLst.append((r + 1, c))
                if maze[r][c - 1] == path: neighborLst.append((r, c - 1))
                if maze[r][c + 1] == path: neighborLst.append((r, c + 1))
                if (r, c) in neighborDct:
                    neighborDct[(r, c)] += neighborLst
                else:
                    neighborDct[(r, c)] = neighborLst
            elif maze[r][c].isupper():
                code = ''
                if r > 0 and r < len(maze) - 1:
                    if maze[r - 1][c].isupper() and maze[r + 1][c] == path:
                        code = maze[r - 1][c] + maze[r][c]
                        warpPt = (r + 1, c)
                    elif maze[r + 1][c].isupper() and maze[r - 1][c] == path:
                        code = maze[r][c] + maze[r + 1][c]
                        warpPt = (r - 1, c)
                if c > 0 and c < len(maze[r]) - 1:
                    if maze[r][c - 1].isupper() and maze[r][c + 1] == path:
                        code = maze[r][c - 1] + maze[r][c]
                        warpPt = (r, c + 1)
                    elif maze[r][c + 1].isupper() and maze[r][c - 1] == path:
                        code = maze[r][c] + maze[r][c + 1]
                        warpPt = (r, c - 1)
                
                if not code: continue
                if code == 'AA':
                    start = warpPt
                elif code == 'ZZ':
                    end = warpPt
                elif code in warpDct:
                    if warpDct[code] in neighborDct:
                        neighborDct[warpDct[code]] += [warpPt]
                    else:
                        neighborDct[warpDct[code]] = [warpPt] 
                    if warpPt in neighborDct:
                        neighborDct[warpPt] += [warpDct[code]]
                    else:
                        neighborDct[warpPt] = [warpDct[code]]
                else:
                    warpDct[code] = warpPt

                if code in ('AA', 'ZZ'): continue
                if warpPt[0] <= 2 or warpPt[0] >= len(maze) - 3 or \
                    warpPt[1] <= 2 or warpPt[1] >= len(maze[r]) - 3:
                    recurseDct[warpPt] = 1
                else:
                    recurseDct[warpPt] = -1

    q = [(0, 0, start)]
    distDct = {(0, start): 0}
    while q:
        l, d, p = heapq.heappop(q)
        if p == end and l == 0:
            print(d)
            break
        for nbr in neighborDct[p]:
            newL = l
            if p in recurseDct and nbr in recurseDct:
                newL += recurseDct[nbr]
                if newL < 0: continue
            if (newL, nbr) not in distDct:
                distDct[newL, nbr] = d + 1
                heapq.heappush(q, (newL, d + 1, nbr))

main()
