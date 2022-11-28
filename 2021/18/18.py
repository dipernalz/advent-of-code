# 161/1070

from math import ceil

inpt = open('input.txt', 'r').read().rstrip().split('\n')


def add(s, t):
    s = ['['] + to_list(s) + [','] + to_list(t) + [']']
    u = True
    while u:
        u = False

        d = 0
        for i, c in enumerate(s):
            if c == '[':
                d += 1
            elif c == ']':
                d -= 1
            elif c != ',':
                if d >= 5:
                    j = i - 1
                    while j >= 0:
                        if s[j] not in '[],':
                            break
                        j -= 1
                    k = i + 3
                    while k < len(s):
                        if s[k] not in '[],':
                            break
                        k += 1
                    if j != -1:
                        s[j] = str(int(s[j]) + int(s[i]))
                    if k != len(s):
                        s[k] = str(int(s[k]) + int(s[i + 2]))
                    s[i - 1] = '0'
                    del s[i:i + 4]
                    u = True
                    break

        if u:
            continue

        for i, c in enumerate(s):
            if c in '[],':
                continue
            c = int(c)
            if c >= 10:
                s = (s[:i] +
                     ['[', str(c // 2), ',', str(ceil(c / 2)), ']'] +
                     s[i + 1:])
                u = True
                break

    return ''.join(s)


def magnitude(s):
    return 3 * (s[0] if type(s[0]) == int else magnitude(s[0])) + \
           2 * (s[1] if type(s[1]) == int else magnitude(s[1]))


def to_list(s):
    if type(s) == list:
        return s
    s = list(s)
    p = False
    for i, c in enumerate(s):
        if c not in '[],':
            if p:
                s[i - 1] += s[i]
                s[i] = ''
                p = False
            else:
                p = True
        elif p:
            p = False

    return [c for c in s if c]


# Part 1
snailfish_sum = inpt[0]
for line in inpt[1:]:
    snailfish_sum = add(snailfish_sum, line)
print(magnitude(eval(snailfish_sum)))

# Part 2
max_mag = 0
for i in range(len(inpt)):
    for j in range(len(inpt)):
        if i == j:
            continue
        max_mag = max(max_mag, magnitude(eval(add(inpt[i], inpt[j]))))
print(max_mag)
