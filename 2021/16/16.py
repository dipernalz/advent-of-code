# 1236/966

inpt = open('input.txt', 'r').read().rstrip().split('\n')
v_sum = 0

def hex_to_bin(hex):
    b = bin(int(hex, 16))[2:]
    return '0' * (4 - len(b)) + b

def parse(packet):
    global v_sum
    i = 0

    v = int(packet[i:i + 3], 2)
    i += 3
    v_sum += v

    t = int(packet[i:i + 3], 2)
    i += 3

    if t == 4:
        val = ''
        while packet[i] == '1':
            val += packet[i + 1:i + 5]
            i += 5
        return i + 5, int(val + packet[i + 1:i + 5], 2)

    values = []
    l = int(packet[i], 2)
    i += 1
    if l == 0:
        length = int(packet[i:i + 15], 2)
        i += 15
        while length > 0:
            l, val = parse(packet[i:])
            values.append(val)
            i += l
            length -= l
    else:
        n_packets = int(packet[i:i + 11], 2)
        i += 11
        for j in range(n_packets):
            l, val = parse(packet[i:])
            values.append(val)
            i += l

    if t == 0:
        return i, sum(values)
    if t == 1:
        p = 1
        for val in values:
            p *= val
        return i, p
    if t == 2:
        return i, min(values)
    if t == 3:
        return i, max(values)
    if t == 5:
        return i, values[0] > values[1]
    if t == 6:
        return i, values[0] < values[1]
    if t == 7:
        return i, values[0] == values[1]

message = ''.join(hex_to_bin(i) for i in inpt[0])
output = int(parse(message)[1])
print(v_sum)
print(output)
