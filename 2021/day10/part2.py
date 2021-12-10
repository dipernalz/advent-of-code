# 971

inpt = open('input.txt', 'r').read().rstrip().split('\n')

pairs = {')': '(', ']': '[', '>': '<', '}': '{'}
score_map = {'(': 1, '[': 2, '{': 3, '<': 4}

scores = []
for i in inpt:
    stack = []
    corrupt = False
    for c in i:
        if c not in pairs:
            stack.append(c)
        else:
            if pairs[c] != stack[-1]:
                corrupt = True
                break
            stack.pop()
    if corrupt:
        continue

    score = 0
    for c in stack[::-1]:
        score *= 5
        score += score_map[c]
    scores.append(score)

print(sorted(scores)[len(scores) // 2])
