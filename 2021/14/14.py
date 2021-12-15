# 292/89

from collections import Counter, defaultdict

inpt = open('input.txt', 'r').read().rstrip().split('\n\n')

rules = {}
for i in inpt[1].split('\n'):
    a, b = i.split(' -> ')
    rules[a] = b

# Part 1
seq = inpt[0]
for i in range(10):
    nxt = ''
    for j in range(len(seq) - 1):
        if seq[j:j + 2] in rules:
            nxt += seq[j] + rules[seq[j:j + 2]]
        else:
            nxt += seq[j]
    nxt += seq[-1]
    seq = nxt

freq = Counter(seq)
print(max(freq.values()) - min(freq.values()))

# Part 2
seq = inpt[0]
pairs = defaultdict(int)
freq = defaultdict(int)
for i in range(len(seq) - 1):
    pairs[seq[i:i + 2]] += 1
    freq[seq[i]] += 1
freq[seq[-1]] += 1

for i in range(40):
    nxt = defaultdict(int)
    for p in pairs:
        if p in rules:
            nxt[p[0] + rules[p]] += pairs[p]
            nxt[rules[p] + p[1]] += pairs[p]
            freq[rules[p]] += pairs[p]
        else:
            nxt[p] += pairs[p]
    pairs = nxt

print(max(freq.values()) - min(freq.values()))
