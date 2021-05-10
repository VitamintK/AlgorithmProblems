T = int(input())
for t in range(T):
    n, k= map(int, input().split())
    ws = [int(x) for x in input().split()]
    tot = 0
    can = True
    for i in range(n):
        if tot+ws[i] == k:
            if i == n-1:
                can = False
                break
            else:
                ws[i+1], ws[i] = ws[i], ws[i+1]
        tot += ws[i]
    if can:
        print("YES")
        print(*ws)
    else:
        print("NO")
