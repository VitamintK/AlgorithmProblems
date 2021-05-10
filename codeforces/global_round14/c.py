from heapq import heappush, heappop
T = int(input())
for t in range(T):
    n,m,x = map(int, input().split())
    hs = [int(h) for h in input().split()]
    ms = []
    ans = []
    for i in range(m):
        heappush(ms, (0,i))
    for i in range(n):
        h = hs[i]
        c, tower = heappop(ms)
        ans.append(tower+1)
        heappush(ms, (c+h, tower))
    print("YES")
    print(*ans)