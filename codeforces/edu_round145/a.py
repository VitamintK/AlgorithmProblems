import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    s = input().strip()
    if len(set(s)) == 1:
        print('-1')
    elif len(set(s))==4:
        print(4)
    elif len(set(s))==3:
        print(4)
    else:
        c = dict()
        for x in s:
            if x not in c:
                c[x] = 1
            else:
                c[x] += 1
        if c[x] == 2:
            print(4)
        else:
            print(6)