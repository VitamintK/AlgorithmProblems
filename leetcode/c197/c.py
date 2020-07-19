from heapq import heappush, heappop
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj = [[] for i in range(n)]
        for i in range(len(edges)):
            a, b = edges[i]
            c = succProb[i]
            adj[a].append((b, c))
            adj[b].append((a, c))
        visited = set()
        pq = [(-1, start)]
        while len(pq) > 0:
            ex = heappop(pq)
            prob, v = ex
            visited.add(v)
            if v == end:
                return -prob
            for u, c in adj[v]:
                if u in visited:
                    continue
                heappush(pq, (prob*c, u))
        return 0