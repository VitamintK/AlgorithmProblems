def get_all_g(n):
    for i in range(pow(2,n)):
        ans = set()
        j = 0
        while i > 0:
            if i%2 == 1:
                ans.add(j)
            j += 1
            i //= 2
        yield ans

def dfs(g,edges,visited, b):
    visited.add(b)
    maxd = (0,b)
    for v in edges[b]:
        if v in visited:
            continue
        if v not in g:
            continue
        dist, f = dfs(g,edges,visited,v)
        maxd = max(maxd, (dist+1, f))
    return maxd
        
def get_diam(g, edges):
    if len(g) == 0:
        return -1
    visited = set()
    b = g.pop()
    g.add(b)
    dist, f = dfs(g, edges, visited, b)
    dist, ff = dfs(g, edges, set(), f)
    # print(g, dist)
    if len(visited) != len(g):
        return -1
    return dist
        
class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = [[] for i in range(n)]
        for u,v in edges:
            adj[u-1].append(v-1)
            adj[v-1].append(u-1)
        ans = [0 for i in range(1,n)]
        for g in get_all_g(n):
            x = get_diam(g, adj)
            if x == -1 or x == 0:
                continue
            ans[x-1] += 1
        return ans