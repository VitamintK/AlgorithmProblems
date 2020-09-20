from heapq import heappush, heappop
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = [[0 for j in range(len(points))] for i in range(len(points))]
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                edges[i][j] = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
                edges[j][i] = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
        inf = 1234567890
        # distances = [inf for i in range(n)]
        frontier = [(0, 0)]
        gotem = set()
        ans = 0
        while len(frontier) > 0:
            cost, ex = heappop(frontier)
            if ex in gotem:
                continue
            ans += cost
            gotem.add(ex)
            for i in range(len(points)):
                if i not in gotem and i != ex:
                    heappush(frontier, (edges[ex][i], i))
        return ans
        
                