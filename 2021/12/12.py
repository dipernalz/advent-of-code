# 49/303

from collections import defaultdict, deque

inpt = open('input.txt', 'r').read().rstrip().split('\n')

graph = defaultdict(set)
for i in inpt:
    a, b = i.split('-')
    graph[a].add(b)
    graph[b].add(a)

# Part 1
q = deque([('start', set())])
n = 0
while q:
    node, visited = q.pop()
    if node == 'end':
        n += 1
        continue
    visited.add(node)
    for nbr in graph[node]:
        if nbr.isupper() or nbr not in visited:
            q.append((nbr, visited.copy()))
print(n)

# Part 2
q = deque([('start', set(), False)])
n = 0
while q:
    node, visited, repeat = q.pop()
    if node == 'end':
        n += 1
        continue
    visited.add(node)
    for nbr in graph[node]:
        if nbr.isupper() or nbr not in visited:
            q.append((nbr, visited.copy(), repeat))
        elif nbr != 'start' and not repeat:
            q.append((nbr, visited.copy(), True))
print(n)
