# 1152

inpt = open('input.txt', 'r').read().rstrip().split('\n')

pairs = {')': '(', ']': '[', '>': '<', '}': '{'}
score_map = {')': 3, ']': 57, '}': 1197, '>': 25137}

n = 0
for i in inpt:
    stack = []
    for c in i:
        if c not in pairs:
            stack.append(c)
        else:
            if pairs[c] != stack[-1]:
                n += score_map[c]
                break
            stack.pop()

print(n)
