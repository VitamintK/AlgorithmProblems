class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adj = [[] for i in range(n)]
        for u,v in roads:
            adj[u].append(v)
            adj[v].append(u)
        ans = 0
        for i in range(len(adj)):
            for j in range(i+1, len(adj)):
                x = len(adj[i]) + len(adj[j])
                if j in adj[i]:
                    x -= 1
                ans = max(ans, x)
        return ans