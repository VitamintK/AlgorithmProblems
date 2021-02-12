n = int(input())
edges = [[] for i in range(n)]
total = 0
for i in range(n-1):
    u, v, p = map(int, input().split())
    edges[u].append((v,p))
    edges[v].append((u,p))
    total += p

ans = total
for i in range(n):
    vals = [p for v,p in edges[i]]
    sm = sum(vals)
    mx = max(vals)
    if mx > sm-mx:
        save = sm-mx
    else:
        save = sm//2
    ans -= save
print(ans)