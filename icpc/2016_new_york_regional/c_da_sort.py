#LIS?

T = int(input())
for t in range(T):
    n = int(input().split()[1])
    L = []
    for i in range((n+9)//10):
        L.extend([int(x) for x in input().split()])
    pt = 0
    LL = sorted(L)
    for i in L:
        if i == LL[pt]:
            pt += 1
    print(t+1, n - pt)
