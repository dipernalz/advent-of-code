import re
from functools import cache

inpt = open('input.txt', 'r').read().rstrip().split('\n\n')

rules = {}
for i in inpt[0].split('\n'):
    a, b = i.split(': ')
    if '"' in b:
        rules[a] = b[1]
    else:
        rules[a] = [j.split() for j in b.split(' | ')]

messages = inpt[1].split('\n')

# Part 1
@cache
def generate_re(rule):
    if type(rules[rule]) == str:
        return rules[rule]

    reg_exp = ''
    for s in rules[rule]:
        reg_exp += '|'
        for r in s:
            reg_exp += generate_re(r)

    return f'({reg_exp[1:]})' if len(rules[rule]) > 1 else reg_exp[1:]

print(sum(1 for m in messages if re.fullmatch(generate_re('0'), m)))

# Part 2
@cache
def generate_re(rule):
    if rule == '8':
        return f'{generate_re("42")}+'
    if rule == '11':
        return '(' + ''.join(
            f'|{generate_re("42")}{{{i}}}{generate_re("31")}{{{i}}}'
            for i in range(1, 5))[1:] + ')'

    if type(rules[rule]) == str:
        return rules[rule]

    reg_exp = ''
    for s in rules[rule]:
        reg_exp += '|'
        for r in s:
            reg_exp += generate_re(r)

    return f'({reg_exp[1:]})' if len(rules[rule]) > 1 else reg_exp[1:]

print(sum(1 for m in messages if re.fullmatch(generate_re('0'), m)))
