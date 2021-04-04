T = int(input())
for t in range(T):
    n = int(input())
    s = input()
    can = True
    if s.count('0')%2 == 1:
        can = False
    elif n%2 == 1:
        can = False
    elif s[0]=='0' or s[-1]=='0':
        can = False
    if not can:
        print("NO")
        continue
    parity = 0
    pdict = {0: '()', 1: ')('}
    a = []
    b = []
    h = 0
    for i in range(n):
        if s[i] == '0':
            a.append(pdict[parity][0])
            b.append(pdict[parity][1])
            parity = 1-parity
        elif i == n-1 or h >= 2:
            a.append(')')
            b.append(')')
            h -= 1
        else:
            a.append('(')
            b.append('(')
            h += 1
    print('YES')
    print(''.join(a))
    print(''.join(b))