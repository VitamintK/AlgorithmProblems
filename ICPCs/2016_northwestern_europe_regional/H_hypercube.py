n, a, b = input().split()
n = int(n)
def get_position(bs):
    pos = 0
    parity = 1
    for index, bit in enumerate(bs):
        segment = pow(2,len(bs)-index - 1)
        if bit == '1':
            pos += segment*parity
            parity = 1-parity
        else:
            pos += segment * (1-parity)
    return pos
print(get_position(b) - get_position(a) -1)
