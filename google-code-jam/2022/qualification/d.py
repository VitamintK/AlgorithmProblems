import sys
sys.setrecursionlimit(200000)

def dfs(children, fs, i):
    """returns (the smallest possible fun factor rooted at i, sum)"""
    if len(children[i])==0:
        return fs[i], fs[i]
    agg = 0
    ans = []
    for child in children[i]:
        smallest, sm = dfs(children, fs, child)
        ans.append(smallest)
        agg += sm
    mn = min(ans)
    if fs[i] > mn:
        agg += fs[i] - mn
    return max(fs[i], mn), agg

T = int(input())
for t in range(T):
    n = int(input())
    fs = [0] + [int(x) for x in input().split()]
    ps = [int(x) for x in input().split()]
    children = [[] for i in range(n+1)]
    for i, p in enumerate(ps):
        children[p].append(i+1)
    _, ans = dfs(children, fs, 0)
    print(f"Case #{t+1}: {ans}")
    
