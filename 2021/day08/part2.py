# 435

inpt = open('input.txt', 'r').read().rstrip().split('\n')

n = 0
for i in inpt:
    patterns, output = i.split(' | ')
    patterns = [set(j) for j in sorted(patterns.split(), key=len)]

    nums = {}
    nums[1] = patterns[0]
    nums[7] = patterns[1]
    nums[4] = patterns[2]
    nums[8] = patterns[-1]
    for j in patterns:
        if len(j) == 5:
            if j.intersection(nums[1]) == nums[1]:
                nums[3] = j
            elif len(j.intersection(nums[4])) == 3:
                nums[5] = j
            else:
                nums[2] = j
        if len(j) == 6:
            if j.intersection(nums[7]) != nums[7]:
                nums[6] = j
            elif len(j.intersection(nums[4])) == 4:
                nums[9] = j
            else:
                nums[0] = j
    s = []
    for j in output.split():
        for k in nums:
            if nums[k] == set(j):
                s.append(str(k))
    n += int(''.join(s))
print(n)
