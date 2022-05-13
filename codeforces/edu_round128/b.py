T = int(input())
for t in range(T):
    n,m = map(int, input().split())
    bots = []
    for i in range(n):
        r = input()
        for j in range(m):
            if r[j]=='R':
                bots.append((i,j))
    ans = False
    for b1 in bots:
        r,c = b1
        dominant = True
        for r2,c2 in bots:
            if r2 < r or c2 < c:
                dominant = False
                break
        if dominant:
            ans = True
            break
    if ans:
        print("YES")
    else:
        print("NO")