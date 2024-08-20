import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    n = int(input())
    if n % 2 == 0:
        print(-1)
    else:
        l = [0 for i in range(n)]
        p = n//2
        parity = -1
        for i in range(n):
            l[p] = i+1
            p += parity * (i+1)
            parity *= -1
        print(' '.join(map(str, l)))
