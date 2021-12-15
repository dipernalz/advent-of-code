# 275/195

inpt = open('input.txt', 'r').read().rstrip().split('\n\n')

nums = inpt[0]
nums = list(map(int, nums.split(',')))

boards = inpt[1:]
boards = [[list(map(int, c.split())) for c in b.split('\n')] for b in boards]
boards = [b[0] + b[1] + b[2] + b[3] + b[4] for b in boards]

constraints = []
for i in range(0, 25, 5):
    constraints.append(set(range(i, i + 5)))
for i in range(5):
    constraints.append(set(range(i, i + 25, 5)))

# Part 1
marked = [set() for i in range(len(boards))]
f = False
for n in nums:
    for b in range(len(boards)):
        if n in boards[b]:
            marked[b].add(boards[b].index(n))
    for c in constraints:
        if f:
            break
        for b in range(len(boards)):
            if 5 == len(marked[b].intersection(c)):
                x = sum(boards[b][i] for i in range(len(boards[b]))
                        if i not in marked[b])
                print(n * x)
                f = True
                break

# Part 2
marked = [set() for i in range(len(boards))]
wins = set()
f = False
for n in nums:
    for b in range(len(boards)):
        if n in boards[b]:
            marked[b].add(boards[b].index(n))
    for c in constraints:
        if f:
            break
        for b in range(len(boards)):
            if b in wins:
                continue
            if 5 == len(marked[b].intersection(c)):
                wins.add(b)
                if len(wins) == len(boards):
                    x = sum(boards[b][i] for i in range(len(boards[b]))
                            if i not in marked[b])
                    print(n * x)
                    f = True
